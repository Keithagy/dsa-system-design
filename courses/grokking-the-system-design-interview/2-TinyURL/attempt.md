# Designing TinyURL

This service will provide short aliases redirecting to long URLs.

Difficulty Level: Easy

## Practice

### Requirements clarifications

#### Questions

- Should you be able to customize this link?
  - What parameters should you be able to customize?
  - Should we be able to identify who routed to a location, based on certain properties in the link?
  - Do we need to ensure link generations follow some kind of randomized or unpredicatable pattern, within customization bounds?
- What uptime tradeoffs we are willing to accept with this system?
  - It seems like we need to minimize the experience of links appearing down when they are actually up. Likely need to minimize downtime
- What are the core functionalities to build out, and what are the functionalities that can be planned into later phases or scoped into a subsequent version?
  - Core functionalities:
    - URL shortening
    - Link customization (e.g. `myCompany-short.en/{linkID}`)
    - Reliably resolving shortened URLs to endpoints
    - Managing link expirations
  - Later-phase functionalities:
    - Click analytics
    - Identifying short-link usage patterns
- Is there any event-driven functionality to this system?
  - Link access notification
  - Link expiration

#### Functional Requirements

- Capable of generating short URLs
  - Pass in a full url, get back a shortened one that is a human-readable length
- Customize short URLs to follow certain routing schema
  - Would likely require a custom DNS server
- Managing URL expirations
- Managing click analytics
- Handling events with notifications
  - Link access notification
  - Link expiration notification

#### Non-Functional Requirements

- Need high uptime
- Redirects should be of minimal observability to the user
  - If our systems need to run any analytics logic in response to a click, it should not block the redirect?

#### Scoped out

- Functionalities that might sensibly block the redirect

  - Validation surrounding link access hours
  - Validation around number of times link can be accessed
  - Device-dependent rerouting
  - For now, as a rule we scope out click behaviors that can potentially block the redirect, because we want to prioritize a high-uptime, low-latency system, and introducing logic that blocks the redirect would impede that

- Since we are talking about a http routing layer, we can also make it a point that we will only support redirecting GET calls
  - We could imagine supporting pasting a certain short link into an application that would allow for that to be used as a custom endpoint instead of some predefined default, but that would require us to reroute post calls which would likely have different middleware-dependent requirements.

### Back-of-envelope estimation

- What order of magnitude of traffic are we aiming to support?
- Is this a read-heavy or write-heavy system?
- Are there characteristics about the access pattern that we can exploit?

- Let's say the average link gets visited 50 times a day.
  - However, the distribution around this average is not uniform.
  - You probably have a small number of popular links (let's say 5%) that get visited tens of thousands+ times a day, and most links getting visited no more than 10 times a day
  - 5% of the links would account for 99+% of the load. >> to revisit re: implications on caching mechanism
  - Across time, the frequency with which a link gets access probably also decreases.
- Read/write characteristics of this system:
  - Dominant operation would likely be resolving a given shortlink id to a given full URL (read operation)
  - Any other read operations?
    - Admin-related reads (e.g. listing down all active urls for a given account, checking url expirations, etc.)
    - Internal analytics workflows which would likely happen in large batches, but would access data in a much more uniform way across time and identifier bounds than normal users
    - However, we can afford for this to be slower, or to maintain this via a chron-based batch replication, if we need to make tradeoffs.
- If we say that we are going to have thousands of companies, each with 100 links on average, that means we will need to track ~100k links and be ready for about ~5m link accesses per day.

### System interface definition

The interface here is probably mainly the custom short links.
Indicative default structure:
`short.en/${linkId}`

If we want to support customization, we could perhaps do so as a subdomain under our main `short` one:
`myCompany.short.en/${linkId}`

We would likely need an admin web dashboard interface interacting with http endpoints exposed by services fronting our databases:

- Link creation / inspection / deletion
- Defining expiration
- Checking access analytics
- Defining notification strategies in relation to specific links

### Defining Data model

The core model is likely a `ShortLink`:

```json
{
  "id": "uuid", // specific convetion TBD
  "destination": "url", // Where the short link redirects to
  "owner": "uuid", // The account that owns this link
  "expires": "datetime", // expiration
  "customization": "uuid" // foreign key to a customization data model
}
```

An owner can also define `Customization`s to apply to `ShortLink`s:

```json
{
  "id": "uuid",
  "owner": "uuid",
  "subdomain": "string" // If a ShortLink as a customization with subdomain "hello", shortlink will be hello.shorten.me
}
```

Will likely need to expand this to include:

- Which account owns a `ShortLink`
- Notification policies
- Expiration policies
- Customization policies

You have supplementary data models around accounts and notifications that we can just handwave for now.

### High level / detailed design

The bulk of our system should be shortlink redirector service instances, deployed in parallel.
They receive a shortLink Id and respond with a redirect response to the correct URL.
In other words, these would be stateless services without concerns around request routing.
They would be able to deliver a full response based on the linkId specified in the initial request.
You would need an API gateway fronting the cluster, so that `short.en` calls have a clear target to route toward.

This API gateway can also sufficiently serve as the load balancer for our redirector instances.
However, this does make the API gateway a critical point of failure -- if it goes down then none of our redirectors would be reachable.
We can address this either by benchmarking to allocate a deep enough compute resource to this gateway, and then additionally by keeping a container in reserve ready to take over should a given gateway go down, or we can define horizontally scalable replications of the API gateway. This would be doable considering that

The redirector service instances would all come with their own read-only replicas of the shortlinks database, and the shortlinks database would be modifiable via an admin panel and associated endpoints.

You can probably also use a LFU cache to reduce load on the database, since there is a virality to link access that we can take advantage of.

expiration:

- Chron-based timestamp checks for expiration
- Apply lazy eval, delete and mark 404 only if read and found to be past expiration.
- Retain read-only nature of system by providing an event bus such as Amazon EventBridge, SQS, Kafka, that routes delete events back to an event-driven cleanup service
- Can also use this mechanism to route notifications for link access
- Minimize redirect latency deferring telemetry / analytics to appropriate event streams

### Bottlenecks and markers of system outliving its age

- redirect-blocking functionality becomes critical
- shortlink dataflows ever, for whatever reason, become stateful
