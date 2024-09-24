# Designing Data Intensive Applications

<!--toc:start-->

- [Designing Data Intensive Applications](#designing-data-intensive-applications)
  - [Part 1: Foundations of Data Systems](#part-1-foundations-of-data-systems)
    - [Chapter 1: Reliable, Scalable and Maintainable Applications](#chapter-1-reliable-scalable-and-maintainable-applications)
      - [Thinking about data systems](#thinking-about-data-systems)
      - [Reliability](#reliability)
      - [Scalability](#scalability)
      - [High-level scalability considerations](#high-level-scalability-considerations)
      - [Maintainability](#maintainability)
        - [Operability](#operability)
        - [Simplicity](#simplicity)
        - [Extensibility](#extensibility)
    - [Chapter 2: Data Models and Query Languages](#chapter-2-data-models-and-query-languages)
      - [Relational vs Document Model (or SQL vs NoSQL)](#relational-vs-document-model-or-sql-vs-nosql)
      - [Do you need ACID or BASE?](#do-you-need-acid-or-base)
    - [Chapter 3: Storage and Retrieval](#chapter-3-storage-and-retrieval)
      - [Important Database-Related Data Structures](#important-database-related-data-structures)
        - [LSM-Trees vs B-Trees](#lsm-trees-vs-b-trees)
        - [Multi-Column Indexes](#multi-column-indexes)
        - [Full-text search and fuzzy indices](#full-text-search-and-fuzzy-indices)
        - [In-memory data stores](#in-memory-data-stores)
        - [OLTP (transaction processing) vs OLAP (analytic systems)](#oltp-transaction-processing-vs-olap-analytic-systems)
        - [Data compression](#data-compression)
    - [Chapter 4: Encoding and Evolution](#chapter-4-encoding-and-evolution)
      - [Compatibility considerations](#compatibility-considerations)
      - [Problems with RPCs](#problems-with-rpcs)
  - [Part 2: Distributed Data](#part-2-distributed-data)
    - [Chapter 5: Replication](#chapter-5-replication)
    - [Chapter 6: Partitioning](#chapter-6-partitioning)
    - [Chapter 7: Transactions](#chapter-7-transactions)
    - [Chapter 8: The Trouble with Distributed Systems](#chapter-8-the-trouble-with-distributed-systems)
    - [Chapter 9: Consistency and Consensus](#chapter-9-consistency-and-consensus)
  - [Part 3: Derived Data](#part-3-derived-data) - [Chapter 10: Batch Processing](#chapter-10-batch-processing) - [Chapter 11: Stream Processing](#chapter-11-stream-processing) - [Chapter 12: Future of Data Systems](#chapter-12-future-of-data-systems)
  <!--toc:end-->

## Part 1: Foundations of Data Systems

### Chapter 1: Reliable, Scalable and Maintainable Applications

Many applications today are data-intensive, not compute-intensive.

Some non-trivial functionalities:

- Store data so that they, or another application, can find it again later (databases)
- Remember the result of an expensive operation, to speed up reads (caches)
- Allow users to search data by keyword or filter it in various ways (search indexes)
- Send a message to another process, to be handled asynchronously (stream processing)
- Periodically crunch a large amount of accumulated data (batch processing)

#### Thinking about data systems

Observe that databases, queues, caches, etc. as being (meaningfully different) variations on a theme, not categorically different tools.

- Databases and message queues might appear to do the same thing -- store data for some time
- However they have very different access patterns, which means different performance characteristics, and thus very different implementations

It's important to be able to fluidly navigate categorizations based on their specific tradeoffs and configurations:

- Redis can be a cache, database or message queue
- Kafka is a message queue with database-like durability guarantees

Boundaries between categories are becoming blurred.

In a data-intensive application, work is often broken down into subtool-optimized tasks that are then executed in parallel before being stitched (reduced) into a final result.

For instance:

- Memcached for application-managed caching layer
- Elasticsearch for full-text search server
- Postgres for main database
- Rabbit MQ for message queuing / writing to some other event handler

In these cases it is often the application code's responsibility to keep those caches and indexes in sync with the main database.
Further, it is the job of that applications API to implement the facade pattern, and hide these implementation details from the clients / users of the service.
Composition yields specialized data systems.

Key focuses of software system design:
**Reliability**: The system should continue to work correctly even in the face of hardware / software faults and human error
**Scalability**: As the system grows, (in data volume, traffic volume, or complexity), there should be reasonble ways of dealing with that growth.
**Maintainability**: Over time, many different people will work on the system (engineering and operations, both maintaining current behavior and adapting the system to new use cases), and they should be able to work with it productively.

#### Reliability

Can the software tolerate the user making mistakes or using the software in unexpected ways?
Does it perform well enough for the required use case, under the expected load and data volume?
Does the system prevent unauthorized access and abuse?

"Fault" and "Failure" are different things:
**Fault**: One system compoenent deviate from spec
**Failure**: System as a whole stops providing required service to user

`Fault` is component-scoped, `Failure` is system scoped.
We are not trying to reduce the probability of a fault to zero;
Rather, we are going for designing fault-tolerance mechanisms that prevent faults from causing failures.

A good way to test your system for fault tolerance is by deliberately triggering them (chaos engineering).
If your system can survive randomly killing individual processes without warning, then you probably are fine.
Well known tool that does this: Netflix's `Chaos Monkey`.

Hard disks have a mean time to failure of about 10 to 50 years.
Thus, on a storage cluster with 10,000 disks, we should expect on average one disk to die per day.

First response is usually to build redundancy into hardware.

- Disks maybe set up in a RAID configuration
- Servers may have dual power supplies
- May also have hotswappable CPUs
- Data centers may have backup power generators

With these types of faults in the hardware underlying virtual machines (which we interact with via containers), it is not uncommon for the virtual machines themselves to randomly die too.
System design should accomodate the loss of entire machines.

#### Scalability

Increased load (beyond expected bounds) is a common reason for degradation.
Scalability refers to the ability of the system to cope with increased load.

However, it is not a one-dimensional label.
Meaningless to say that "X is scalable" or "Y does not scale".
You always need to talk about what you are scaling with respect to.

- Traffic volume
- Payload size
- Cognitive complexity
- Maximum size of dataset
- etc

If the system grows in a particular way, what are our options for coping with the growth?

For instance, the main challenge with Twitter isn't with handling spikes in writes, but rather in handling the associated _fan-out_:

- Each user follows many people, and is followed by many people
- Consider two competing implementations of a tweet write:
  - Option 1
    - Insert tweet into a global collection of tweets.
    - When user requests their home timeline, look up all the people they follow
    - Find all the tweets of each of those users
    - Merge them (sorted by time).
  - Option 2
    - Maintain a cache for each user's home timeline -- like a mailbox of tweets for each recipient user
    - When a user posts a tweet, look up all the people who follow that user
    - Insert the new tweet into each of their home timeline caches.
    - Request to read the home timeline is then cheap, because its result has been computed ahead of time.
- Approach 2 allows for much faster reads, but at what cost?
  - Posting a tweet now requires a lot of extra work.
  - On average, a tweet is delievered to 75 followers, so 4.6k tweets per second is 345k writes per second to the home timeline caches.
  - However, this average hides large variation in follower count; some users have over 30 million follows
  - A single tweet may result in over 30 million writes to home timelines

In the example of Twitter, the distribution of followers per user (perhaps weighted by how often those users tweet) is a key load parameter for discussing scalability, since it determines the fan-out load.
More generally, **try to identify key metrics for determining load, that capture the data read/write patterns specific to that platform.**

Final twist of Twitter anecdote: Twitter actually uses a hybrid approach, in which most users' tweets are fanned out to home timelines (because they aren't associated with such a large write load), but a small number of users with a very large number of followers are excepted from this fan-out. Celebrities are fetched separately and merged with the user's home timeline view.

How do we reason about performance in a scalability context?

- When you increase a load parameter and keep the system resources (CPU, memory, network bandwidth etc) unchanged, how does performance metrics of the system get affected?
- When you increase a load parameter, how much additional resources do you need to keep performance unchanged?

You cannot answer either question without thought to how to operationalize performance as a variable -- usually, _response time_ is a good place to start with online systems.

However, sometimes we also care about _throughput_, with compute-bound systems such as Hadoop (number of records we can process per second, or total time needed to run a job on a dataset of a certain size.)

> Definitions:
>
> Latency: Duration that a request spends waiting to be handled -- during which it is latent, awaiting service.
>
> Response time: What the client actually experiences; Besides the actual time to process the request (the service time), includes network delays and queue-ing delays.

Response time follows a distribution, owing to possible environmental failures:

- Context switch to background process
- Loss of network packet / TCP retransmission
- Garbage collection pause
- Cache miss

Performance reported in p{n} response times, percentiles.
Median (p50) is a good metric for the typical request, p99 tells you the tail-end

High percentiles (e.g p999) are important yardsticks of user experience, because those requests frequently have the most data / correspond to the most important payloads for the business.

- E.g. p999 might be only 1 in 1000 requests but for Amazon, this is probably the customer with the largest order history / average cart size
- Optimizing tail end response time is often difficult, because random factors outside of your consider weigh in heavily.
- Tail end is also important to optimize because it often only takes one slow internal network call to slow down serving a composite request.
- Also, if you have 3 calls happening in a chain, and they all have p99 response of 1 second, that means every one of those calls has a 1% chance of taking more than 1 second, that means the total chance of the whole call taking less than 1 second is actually ((0.99)\*(0.99)\*(0.99)) = ~97%

Smart architectures often balance between vertical and horizontal scaling depending on what is most appropriate, because horizontal scaling is often very complex.
Systems that scale horizontally are called _elastic_; vertical scaling often runs into the roadblock of cost because past some point, powerful machines are prohibitively expensive.

When designing a distributed system, think about the specific problems of your system:

- Volume of reads
- Volume of writes
- Volume of data to store
- Complexity of dataflow
- Response time requirements
- Dynamics in data (e.g. virality, power law patterns)

A system that is designed to handle 100,000 requests per second, each 1kB in size, looks very different from a system that designed for 3 requests per minute, each 2GB in size, even though the two systems have the same data throughput.

#### High-level scalability considerations

- Ask yourself if your core dataflows are I/O bound or compute bound
- Given data access patterns, should you prefer availability or consistency, given a network partition? If we don't have a network partition, should you prefer lower latency or consistency?
- Ask yourself where the sweet spot lies when it comes to data partitioning and data replication
- Consider failover mechanisms, especially when it comes to stateful dataflows

#### Maintainability

Relevant principles:

- **Operability**: Make it easy for ops teams to keep system running smoothly.
- **Simplicity**: Make it onboarding-friendly, use as few moving parts as possible (also makes it easier to understand where things might be going wrong).
- **Extensibility**: Make it easy for engineers to make changes to the system in the future.

##### Operability

- System health checks, alarm mechanisms for when services go (seriously) down, past capacity for self-healing
- Inspecting traces for cause of problems
- Keeping software and platforms up to date, including security patches
- Making it easy to reason about how different systems affect each other, so that the impact of problematic changes can be isolated
- Automating migrations
- Keeping a team-level knowledge bank, as a way to preserve organizational knowledge about the system

Measures that can help:

- Provide good observability into runtime behavior and system internals
- Integrate with automated tools for incident notification and tracking
- Avoiding dependency on individual mechanisms (having robust failover strategies)
  - You don't have to always choose to spend something to eliminate a single point of failure
  - However, you do have to always acknowledge the single point of failure and consider if eliminating it is worth the cost
- Providing self-healing strategies as baseline safety nets

##### Simplicity

- See if you are always using the fewest possible number of abstractions to meet requirements.
- Parsimonious design is king

##### Extensibility

- Making change easy; patterns of legacy displacement

In practice (or in interview), scalability and reliability probably matter most.

### Chapter 2: Data Models and Query Languages

Data models are critical to developing good software.
In a system design, they are probably worth devoting a lot of thought to.
The data model tells you how the team is thinking about the problem, but also what dataflows are likely to dominate.
They also present good opportunities for data-oriented software design (pay attention to byte alignments of structs and such).

Key general-purpose data models to familiarize with:

- Relational
- Document
- Graph-based

#### Relational vs Document Model (or SQL vs NoSQL)

Relational Model:

- Best known example is SQL
- Data is organized into _relations_ (called _tables_ in SQL)
- Each relation is an unordered collection of _tuples_ (_rows_ in SQL)
- Better support for joins, and many-to-one and many-to-many relationships

Document Model:

- Sometimes closer to the application model of an entity
- Scalability to very large datasets, or very high write throughput (due to better locality of data fields), generally exceeds relationally modelled data
- Specialized query operations that aren't well supported by relational model
- Popular ones:
  - Key-value
  - Wide-column
  - Document
  - Graph
- Generally allows for greater flexibility in the shape of the data being persisted (since it's not rows with an enforced schema)
- Good for when your entity models are nested, but self-contained (i.e relationships between documents are rare)

Graph databases are kind of the opposite to documents in that they are good for use cases where anything is potentially related to everything

For relations to map nicely to object-oriented programming paradigms, there is often a need to provide an object relation mapping (ORM)

Consider encoding of a resume. You have a few options if you want to stick with SQL:

1. Stick very closely to the relational model and strictly translate lists as one-to-many foreign key mappings and so on
2. Use jsonb in your schema
3. Save resume content as unstructured blob in a column

Alternatively, you can use a document-style store which can model your data much more intuitively as nested json objects.

- Consider if the lack of a schema is an advantage in the particular data/flows you are trying to model

In some situations (e.g. resume jobs), a document-style representation is going to have much better _locality_ than the multi-table schema in typical (strict) SQL.

- If you want to keep nested collections in a relational model, then you need to decide how normalized you want your data to be
- If you are going to fully normalize everything, then prepare for join calls (slower reads)
- If you're going to fully denormalize / duplicate everything, then prepare for repeated writes (slower writes + potential for data inconsistencies)
- Consider how well your data model handles join calls, and consider the interconnectedness of entities in your application
- You can use a document model to represent nested entities, but you still do require a join call if your model requires that you reference a different entity by its ID in the system (e.g. if you need to link to a profile)
- Document databases generally work well for one-to-many relationships (e.g. jobs held by an individual), but many-to-many relationships (e.g. all companies worked at by graduants of a particular collection of a university) could be more difficult.
  - Graph databases might be helpful for such a situation

#### Do you need ACID or BASE?

ACID:

- Atomic >> All operations in a transaction succeed, or every op is rolled back.
- Consistent >> Databases remain in a consistent state before and after every transaction.
- Isolated >> Concurrent transactions do not interfere with each other.
  - There are different isolation levels, that handle racing transactions differently.
  - Suppose you have a case where you have two racing transactions being processed in parallel, one to update and one to delete.
  - There are several standard isolation levels; Higher isolation levels provide more consistency at the expense of concurrency and performance
    - Read uncommitted (lowest isolation)
    - Read committed
    - Repeatable read
    - Serializable (Highest isolation)
  - At lower isolation levels, unpredicatable results could occur
    - Update might succeed on a record that's simultaneously being deleted
    - Delete might remove a record that's being updated
  - At higher isolation levels:
    - Database would typically use locking mechanisms to prevent conflicts
    - Transactions would likely be queued per some order of precedence
  - Sample concurrency control mechanisms:
    - Locking:
      - Pessimistic locking: Locks resources before accessing them
      - Optimistic locking: Allows transactions to proceed and checks for conflicts at commit time
    - Multi-Version Concurrency Control (MVCC):
      - Maintains multiple versions of data
      - Allows read operations to proceed without blocking write operations
      - If delete commits first, update would fail when it tries to commit later
      - If update commits first, then delete would remove the updated record
    - Timestamp Ordering:
      - Assigns timestamps to transactions and orders them based on these timestamps
- Durable >> Completed transactions persist, even after system failures.

ACID databases prioritize data consistency and integrity. They are typically used in systems where data accuracy is critical (e.g. banks)

- Postgres
- MySQL

BASE:

- Basically Available >> System guarantees availability
- Soft State >> State of the system may change over time, even without input (e.g. there might be a backfilling mechanism)
- Eventual Consistency >> The system will become consistent over time, given that the system doesn't receive input during that time.

BASE systems prioritize availability over partition tolerance over immediate consistency.
Common in large-scale distributed systems where high availability and performance are more critical than perfect consistency.

- Cassandra
- MongoDB
- CouchDB
- DynamoDB

Tradeoffs:

- **Consistency model**: ACID ensures immediate consistency, BASE provides only eventual consistency.
- **Scalability**: BASE generally scale horizontally better than ACID databases (due to data model exhibiting greater locality and thus being more friendly to replication and partitioning)
- **Use cases**: ACID generally with banks, data integrity-critical scenarios, BASE generally for high-traffic web applications, real-time big data, similar scenarios

### Chapter 3: Storage and Retrieval

You need accurate mental models of how different kinds of databases handle storage and retrieval, so you can choose the right one.

There is a big difference between transaction-optimized databases and analytics-optimized ones!

#### Important Database-Related Data Structures

Appending to a file is generally very efficient; many databases internally use a _log_ (as in write-ahead log, which you write to before attempting a particular operation), which is an append-only data file

Generally, reading from a database needs to be better than O(n), you need to use an _index_ to prune the search space

- Adding indexes generally incurs overhead, especially on writes.
- For writes, hard to beat the performance of simply appending to a file (which is what GFS tries to leverage).
- Indices need to be updated every time data is written.
- A new index gives a new column / dimension along which to query the data; you might need a few indexes, or a composite one, in order to access the data the way you need to.
- Allowing your data structure to support append-only write pattern also makes it a lot easier to take checkpoints on the state of your index (in case you need to rebuild it)

A simple hash table can often work if you're doing key-value style storage, with the following limitations:

- Range queries cannot be efficient
- Hash table has to fit in memory

SSTables

- Makes use of sortability of keys to keep a sparser index of keys which allows you to access data in a divide-and-conquer, range-based fashion
- "Sparse" is relative to the total number of rows in the store
- Sorted String Table
- Compaction step makes use of something you can visualize as a mergesort algorithm to maintain sortedness of keys
- Since memory has to be accessed in blocks (where each entry in the index points to the start of a block), you could actually compress data in this same blockwise fashion
- You can make use of self-balancing search trees (e.g. red-black trees, AVL trees, B-trees), to keep the indices sorted. These are called _memtables_
- Past some threshold size, you write the index to disk and start a new one
- Then, when serving a read requests, walk the memtables like a linked list; so they all fit together to make the index
- Main problem with this is that the latest memtable, since it is kept in memory, gets lost in the event of a crash.
- Remedy this with a write-head log that, in the event of a crash, replays the log starting from the latest disk-saved memtable to rebuild the state.

LSM-Trees

- Log-structured Merge-Tree, designed for write-optimized database systems; This is a tiered, compacted sequence of SSTables
  - High level idea: keep a cascade of SSTables that are merged in the background
- Arises from SSTables
- Picture a full-text index
  - Given a word in a search query, find all the documents that mention the word
  - Implemented with a key value structure where the key is a word (a term) and the value is the list of IDs of all the documents that contain the word
- Ascertaining a key doesn't exist in the database can be slow;
  - In a naive implementation, you'd have to check every memtable all the way back to the oldest to be sure
  - To optimize for this kind of access, storage engines often use additional _bloom filters_, which can tell you with certainty if an element is _not_ in a set

B-Trees

- Whereas log-structured indexes break the database into variable-size segments and write a segment sequentially, B-trees break the database down into fixed-size _blocks / pages_, and read / write one page at a time.
- Each page can be identified using an address / location, which allows pages to refer to one another. This allows for composition of pages into a tree structure
- You have one page designated the root, and the page contains several keys and page references
  - However, only the leaf pages contain values!
  - In intermediary pages, keys are there as bookends that tell you the range of a given page being referenced, they do not however contain the value "inline"
  - Reading always traverses a B-tree down to a leaf page
- Child page references are organized by continuous range of keys, and the keys on a given page would be bookends for that sub-range
- Key parameter of B-Tree
  - **Branching factor**: how many child pages a given page points to. Typically it is several hundred.
- Updating a value in a B-tree is a matter of using the range property to narrow down to the leaf page and then updating + committing the new value
- To add a new key, you need to find the page whose range encompasses the new key and add it to that page.
- If there isn't enough free space in the page to accommodate the new key, it is split into two half-full pages, then the parent page is updated to account for the new subdivision of key ranges
  - Allows B-trees to always remain balanced; depth is always O(log n)
  - Reference: A 4-level tree of 4KB pages with a branching factor of 500 can store up to 256 TB
- B-trees are not append-only; you do overwrite pages whilst keeping references to that page intact
- If a B-tree crashes after only some of the pages of a write operation have been written (e.g. if you need to split a full leaf page):
  - You might end up with a corrupted index, orphaned pages that don't have a parent, etc
  - In order to make the database resilient, a common strategy is a _write-ahead log_, which is append-only and keeps track of what _should be_ operations committed
  - If a database comes back up after a crash, this log is replayed to restore the B-tree
- Databases sometimes use a copy-on-write scheme, where instead of mutating the thing it's supposed to write over, it writes at a new location, and copy existing data over only the next time it is accessed (in the interim, marking with some tombstone-like value)
- Key abbreviation such that access leverages the context embedded in the access path

##### LSM-Trees vs B-Trees

Reasons why LSM trees are gaining acceptance:

1. Write performance: LSM trees excel at handling high volumes of writes and updates.
2. SSD optimization: Their write pattern is well-suited for SSDs, reducing wear.
3. Compression: LSM trees often achieve better compression ratios.
4. Scalability: They can handle very large datasets efficiently.

Reasons why B-trees remain more common:

1. Read performance: B-trees generally offer better read performance, especially for point queries.
2. Predictable performance: B-trees provide more consistent performance across operations.
3. In-place updates: B-trees allow for in-place updates, which can be advantageous in certain scenarios.
4. Maturity: B-trees have been around longer and are well-understood by developers and database administrators.
5. Transactional support: Traditional B-tree based systems often have better support for complex transactions.

Key factors influencing the choice:

1. Workload characteristics:
   - Write-heavy workloads favor LSM trees.
   - Read-heavy or balanced workloads often favor B-trees.
2. Consistency requirements:
   - B-trees can offer stronger consistency guarantees more easily.
   - LSM trees may require additional mechanisms for strong consistency.
3. Hardware considerations:
   - SSDs benefit more from LSM trees' write patterns.
   - Traditional HDDs may still benefit from B-trees in some cases.
4. Operational complexity:
   - LSM trees require background processes like compaction, which adds operational overhead.
   - B-trees are generally simpler to manage and reason about.
5. Specific use cases:
   - Time-series data often works well with LSM trees.
   - OLTP (Online Transaction Processing) systems often use B-trees.
6. Historical inertia:
   - Many existing systems and skills are built around B-trees.
   - Transitioning to LSM trees can require significant changes in system design and operational practices.
7. Latency requirements:
   - B-trees often provide more predictable and lower worst-case latencies.
   - LSM trees can have occasional high-latency operations due to compaction.

In summary, while LSM trees offer significant advantages for write-heavy workloads and are gaining popularity in certain domains (like NoSQL databases and time-series databases), B-trees remain more common due to their versatility, predictable performance, and the vast ecosystem built around them. The choice between LSM trees and B-trees often comes down to specific workload characteristics, consistency requirements, and operational considerations.

More detail:

- Advantages of LSM-Trees:
  - More write-friendly, because append-only
  - Generally less write amplification (from compacting), because no need for overwriting
  - Compaction ensures full usage of a given disk block; B-trees are more fragmented / sparser
- Downsides of LSM-Trees:
  - Compaction requires either a background thread or context switches which hamper performance on the critical path (compete for write bandwidth)
  - More broadly, compaction needs to be tuned properly not to bottleneck read and write operations
  - B-trees don't need a compaction step; by design, it is range-friendly and divide-and-conquer friendly
  - B-trees also enforce a single copy of a given entity instance in the entire dataset; attractive for database offering strong transactional semantics

##### Multi-Column Indexes

Goes without saying that the primary key of a table takes the form of an index, and that you can build secondary indexes.

However, you can also have multi-column indexes.

- Also called a _concatenated index_.
- Combines several fields into one key by appending one column to another
- Consider the index (lastname, firstname) for a phone book (indexes to hone number)
  - Due to sort order, the index can be used to find all people with a particular last name, or lastname-firstname combination
  - However, it is useless if you want to find all the people with a particular first name
  - Basically, you subset by field in the sort sequence defined.
  - You can't search across firstname because the index has sorted by lastname first.

Good use-case: Searching by location (two dimensions of information)

- Spatial index: R-tree
- Other options are to use a space-filling curve to translate multi-dimensional data to a single number

##### Full-text search and fuzzy indices

Need for functionality such as handling misspellings.

- Usually implemented as some kind of trie-based structure
- Keyword: `Levenshtein automaton`

##### In-memory data stores

- Cache-only stores do not attempt to survive a restart / be durable.
- Sometimes, they come with append-only write-ahead logs that use the disk for durability.
- They are faster not because they never have to read from disk (because in theory, databases with enough memory provisioned never have to, either)
- Rather, they are faster because they don't have to write to disk (and can optimize for that in data structure selection)
- Can also support data models that can be difficult to support in a disk-write-friendly way. Consider Redis for example:
  - Priority queues
  - Sets
- Interesting option for hot data that might exceed RAM: anti-caching approach

##### OLTP (transaction processing) vs OLAP (analytic systems)

- Transactions don't necessarily mean ACID
- In the OLTP context, we're referring only to the size and frequence of read/write ops

| Property             | Transaction processing systems (OLTP)             | Analytic systems (OLAP)                   |
| -------------------- | ------------------------------------------------- | ----------------------------------------- |
| Main read pattern    | Small number of records per query, fetched by key | Aggregate over large number of records    |
| Main write pattern   | Random-access, low-latency writes from user input | Bulk import (ETL) or event stream         |
| Primarily used by    | End user/customer, via web application            | Internal analyst, for decision support    |
| What data represents | Latest state of data (current point in time)      | History of events that happened over time |
| Dataset size         | Gigabytes to terabytes                            | Terabytes to petabytes                    |

OLAP eventually found specialized implementations in data warehouses

- ETL workflows move data from OLTP business-operational systems into OLAP analytics-facing systems
- Warehouses usually organized loosely, soups of facts (fact tables)
- So that analysis can use as see fit
- Labels attached to facts via dimension tables that provide foreign key references to other tables
- Warehouses are usually accessed as a subset of columns; 100s of columns but each query usually only wants 4 or 5
- However you have trillions of rows, which makes the read important to optimize for to the subset of columns queried
- OLTP usually lays out data in a row-wise fashion, but OLAP often lays data out in a column oriented fashion
- If you lay out data in a column oriented fashion, though, then you should be ready to define sort keys on the data because You will need a sort operation which considers entire rows (obviating the benefits of considering individual columns)
- Another way in which data warehouses are optimized are materialized views which essentially precompute common queries (and need to be updated upon write)
- Note: cassandra is wide-column, but not true column-oriented. Clickhouse is true column-oriented

##### Data compression

Bitmap encoding

- Number of distinct values in a column is small relative to the number of rows (e.g. billions of sales transactions but only 100,000s of distinct products)
- If you map each distinct value to a pattern of bits, then you describe the bit pattern in terms of the sequence of 1's and 0's, then you have a shorter representation
- E.g. with run-length encoding
- Queries can then use bitwise AND and OR operations to match the relevant values
- Makes writing to column-oriented storage harder, though
  - If you try to insert a row in the middle of a sorted table with a b-tree index, you will probably need to recompress all the column files

### Chapter 4: Encoding and Evolution

#### Compatibility considerations

Schema changes come with code changes, because the code needs to know how to handle the data.

However, there are roadblocks:

- Server-side applications might have a rollout phase; not all nodes on a system will switch to the latest version from the get go.
- Client-side applications commonly have to deal with version fragmentation.

So we need to maintain compatibility in both directions:

- _Forward compatibility_: Older code can read data that was written by newer code
  - Tends to be harder (especially in situations requiring a change in the API's semantic surface)
- _Backward compatibility_: Newer code can read data that was written by older code.
  - This is not hard; at the baseline you can always keep the old code around to read the old data, subject to some version check

Encodings need to be able to handle both.

- Json does not specify the precision of floating-point numbers, can be arbitrarily large
- IEEE754 double-precision floating-point number cannot represent numbers above 2\^53
- So, every 64-bit and above int is a problem
  - Usually need a string repr
- Json schemas are powerful but rarely used

- Open-closed principle is your friend; old code should just be blissfully unaware of new fields added
- Backward compatibility:
  - If you add a new field, you cannot make it required
  - If you were to add a field and make it required, that check would fail if new code read data written by old code
  - Because the old code will not have written the new field that you added
  - Every field you add after the initial deployment of the schema must be optional or have a default value

If you remove the field:

- You can never remove a required field, because existing code expects it
- You cannot reuse a particular field identifier, because it might break expectations with old code

You can make your schema even more compact by taking the typing information out of the payload, and instead requiring a reader's schema that is compatible to the writer's schema.

#### Problems with RPCs

- They try to make network calls look like local function calls (this abstraction is called location transparency)
- This is a mistake
  - Can't hide network request unpredictabilities >> need things like retry / backoff mechanisms
  - Network calls can timeout, which local calls will never do (though argurably... this is kind of like a lock await that never comes?)
- Retrying non-idempotent network calls can introduce unintended state mutations, which you would not worry about with local function calls
- Network calls can never have arguments passed by reference in the way local calls can; copy operations underlying could impose memory overhead that the mental model hides from the programmer.

To be fair, modern RPC frameworks are more explicit about the over-network nature of the call, and are clearly about encoding that in the interface.

- They also provide ways to await i/o bound tasks that could take a long time to return
- They usually also bundle in serialization to performant encodings like protobuf

#### Message brokers

- Works around subscriptions to stream-like topics
- They don't generally encode any typing (so you have to enforce that in application code)
- They also don't require a response in general, so they might be nice for fire-and-forget style dataflows (rare though they may be)
- Built in QoS features to enforce receipt

#### Distributed actor frameworks

- `Actor` refers to a concurrency model
- Rather than dealing directly with threads and tangling with locking and races,
- Actors are used which represent discrete entities on the system (e.g. clients)
- Actors may hold their own state, and they communicate with other actors by sending and receiving async messages
- Message passing not generally guaranteed to succeed; there might be problems in the send or the receive
- A _distributed_ actor framework simply has nodes communicate in a message passing model over a network, via a message broker

## Part 2: Distributed Data

Part 1 covered aspects of data systems that apply when data is stored on a single machine.
Now we will consider the case of multiple machines being involved in storage and retrieval (and transformation) of data.

Key Metrics:

#### Scalability

If your data volume, read load, or write load grows bigger than a single machine can handle, you can potentially spread the load across multiple machines

#### Fault tolerance / High availability

If your application needs to continue working even if one machine (or several machines, or the network, or an entire data-center) goes down, you can use multiple machines to give you redundancy. When one fails, another one can take over.

#### Latency

If you have users around the world, you might want to have servers at various locations worldwide so that each user can be served from a data-center that is geographically closer to them.
That avoids the users having to wait for network packets to travel halfway around the world.

#### Scaling to higher load

Simplest approach is vertical scaling (throw a bigger machine at the problem). Shared-memory architecture >> all components can be treated as a single machine.

Drawbacks:

- Cost grows faster than linearly; You'll likely also encounter bottlenecks (usually on the transport layer) which gives diminishing marginal returns on vertical scaling, in addition to increasing marginal costs.
- Fault-tolerance is limited, geographic redundancy is nonexistent
- You also have the shared-disk architecture in which independent CPUs and RAM are networked (high-speed) to a shared storage container, but generally the overhead of locking and contention limit the broad applicability of this kind of architecture

The alternative is to share nothing, or to scale out, or to horizontally scale. Use more machines operating in tandem. Distributed systems is about orchestrating these many systems (hard!)

- You can achieve globally distributed low latency and redundancy by spacing your machines out.
- Sometimes data models are off-limits if you need a shared-nothing architecture.

Common ways data is distributed across multiple nodes:

- _Replication_: Keep a copy of the same data on several different nodes, so that data survives some of those nodes going offline / getting destroyed.
- **Partitioning**: Keep different subsets of the data on different nodes, so as to locate / organize the data sympathetically to the way that particular subset of the data is written / read.

### Chapter 5: Replication

Keep a copy of the same data on multiple machines connected via a network.

- Keep data close to where your users are
- Allow system to remain functional even if some parts have failed (increasing availability)
- Scale out number of machines that can serve _read_ queries (thus increasing read throughput)

> Assume for now that dataset can fit in memory; Simplifies things to consider replication in isolation first (we relax this assumption in chapter 6)

Suppose the data being replicated is immutable; replication is easy because you just copy the data to every node, and you're done.
All difficulty lies in tracking and propagating changes to the replicated data; pay attention to the create / update / delete operations.

Popular algorithms for replicating changes between nodes (each with their own tradeoffs):

- Single-leader
- Multi-leader
- Leaderless

#### Leaders and Followers

Every write to the database needs to be processed by every replica, else the replicas would not be replicas!
Most common setup is _leader-based replication_ (also called _master-slave replication_)

1. We designate one of the replicas the leader / master / primary. Clients send write requests to the master, who first writes the new data to its local storage.
2. Other replicas, the followers (also called _hot standbys_), it also sends the data change to all of its followers as part of a _replication log_ or _change stream_.
   Each follower takes the log from the leader and updates its local copy of the database accordingly, by applying all writes in the same order as they were processed on the leader.
3. When a client wants to read from the database, it can query either the leader or any of the followers. However, writes are only accepted on the leader (the followers are read-only from the client's point of view).

#### Asynchronous vs Synchronous Replication

Most relational databases let you configure replication to happen in the background or not.

- The choice here, assuming that you don't have a network partition which prevents your replicas from syncing up, is between having a lower read latency (by letting the client query potentially stale data from a follower), and having strong consistency (by letting the client query wait until a change is confirmed across all replicas before processing it)
- If you do have a network partition, then you can either tell your client that your replica is down (choose consistency) or you can accept serving your client stale data (choose availability)

With respect to the write replication:

- Synchronous replication has the benefit of guaranteeing that the follower has an up-to-date copy of the data before the leader responds to the user's write.
- Stronger redundancy promise.
- However, if the synchronous follower does not respond (because it has crashed, for instance), then the leader cannot respond with a successful write even though it has itself successfully written (because it is prioritizing a strong redundancy promise)
- Thus, impractical for all followers to be synchronous; a single node outage would cause the system to break. In practice, "synchronous replication" usually means you have one synchronous follower and all others asynchronous

Often, if the system wants to prioritize write throughput (availability / lower latency) and trade up consistency, it will replicate asynchronously.

- Writes are not guaranteed to be durable, but leader continues to process writes even if all of its followers have fallen behind.
- This is particularly helpful when dealing with replication lag due to replicas being geographically distributed.

> It can be a serious problem for asynchronously replicated systems to lose data if the leader fails, so researchers have continued investigating methods that don't lose data but still provide good performance and availability.
> One such approach is _chain replication_.
>
> There is a strong connection between consistency of replication and _consensus_ (getting several nodes to agree on a value), which will be explored more later.

#### Setting up New Followers

This is usually done in the background by using a leader snapshot / checkpoint as a starting point, then replaying the leader's replication log from the position that the snapshot is associated with.

#### Follower failure: Catch-up recovery

On its local disk, each follower keeps a log of the data changes it has received from the leader. It can use this log to sync up and replay changes so that it can catch up to the leader in the event of a network disruption.

#### Leader failure: Failover

Leader failure is tricker:

- A follower needs to be promoted to leader
- Client writes need to be rerouted to the new leader
- Replications need to switch to the new leader for reference.

Automatic failover detection:

- Using a healthcheck timeout as an indicator that leader has gone down
- Choosing a new leader
- Reconfiguring the system to use the new leader
  - In particular, getting the old leader (if it comes back) to recognize it is no longer the leader

Things that can go wrong in failover:

- New leader might be behind old leader in the event of async replication.
  - If the former leader leader rejoins the cluster after a new leader has been chosen, what should happen to the divergent writes?
  - Most commonly, old leader's unreplicated writes just get discarded which might not be okay.
- If your new leader doesn't realize some IDs have already been assigned by the old leader (because unreplicated writes) and use those again, then you have a Redis store or something relying on those IDs, you might end up leaking users' data to other users.
- Multiple nodes could believe they are the leader and both accept writes with no way to deconflict after (split brain).
- What is a good leader timeout? Too short, then you have needless failovers. Too long, you have unnecessarily long time to recovery.

Failover is hard to get right and dangerous to get wrong. So, many places actually choose to failover manually.

#### Replication Log Implementations

##### Statement-based replication

Statement-based replication basically streams function calls and parameters, and they get parsed by followers as though they came from client.

- Nondeterminstic functions like `NOW()` and `RAND()` need to be handled differently
- Autoincrements must process in same exact order
- Side-effects must be entirely deterministic

You can generally handle these edge cases but there are so many of them that this is generally a bad idea

##### Write-ahead log shipping

Leader can stream its write ahead log over the network to replicas, and replicas can use that to reconstruct the data
Main disadvantage is that storage engines get coupled, precluding ability to change versions across replicas

##### Row-based (logical) log replication

Same idea as with using the write-ahead log, but decouple from storage engine internals.
Usually a sequence of records describing writes to database tables at the granularity of a row:

- Describe the logical operations. E.g inserted row will describe the new values of all columns
- delete row will contain enough info to uniquely identify the row that was deleted

Idea is that the storage engine can resolve the query, much like statement-based, but the statement is preprocessed to already have the params evaluated
These replications can all be triggered via arbitrary code that watches for changes to certain subsets of the data.

#### Problems with Replication Lag

Leader-based replication requires all writes to go through a single node, but read-only queries can go to any replica.
If your app is read-heavy, then you can increase read throughput just by adding more followers.
However, you need async replication for this to work.
But then your followers might serve reads with stale data! A temporary inconsistency.

If you're okay with _eventual consistency_, then okay.
But this replication lag is potentially unbounded, and might be minutes in systems at capacity.
What are some notable problems that arise with replication lag and how can we solve them?

##### Reading Your Own Writes

People generally are okay with waiting some time to see other people's writes, because they don't know about them.
But they generally want to be able to read their own writes (_read-after-write consistency_)

This is a guarantee that if the user reloads the page, they will always see any updates they submitted themselves.

- Reassures the user that their own input has been saved correctly.

Techniques to implement read-after-write consistency:

- When reading something that the user may have modified, read it from the leader; else, read it from a follower
  - Assumes some ability to know whether something might have been modified without actually querying it
  - E.g. A user's own profile is generally editable only by the user themselves. So, queries by users for their own profile should always be served by the leader.
- Doesn't work if most thing in the application are potentially editable by the user; search for other criteria
  - Client-side state management / query caching
  - Monitor replication lag on followers and prevent queries on any follower too arbitrarily far behind the leader
- The client can remember the timestamp of its most recent write
  - Then the system can ensure that the replica serving any reads for that user reflects updates at least until that timestamp
  - Can also be a _logical timestamp_ (something that indicates ordering of writes, e.g. request ID or log sequence number)
  - Possible to use actual system clock, of course, but then clock synchronization becomes critical
    - E.g. if client machine is very far ahead, it might appear to system like none of the replicas can ever serve properly replicated data
- If you want to use this most-recent-write approach, but want read-after-write consistency across all devices in use by the user, then this last-write timestamp would have to be tracked centrally by the server.

##### Monotonic Reads

When reading from asynchronous follows, it is also possible for a user to see things _moving backward in time_.

This can happen if user makes several reads from different replicas; some reads might hit replicas with updated data, while some reads might hit replicas with stale data.

_Monotonic reads_ is a weaker guarantee than strong consistency, but a stronger one than eventual consistency.
It says that they will not read older data after having previous read newer data.
One way to achieve this is to make sure that each user always makes their reads from the same replica (Different users can read from different replicas).

Replicas can be chosen / routed based on a hash on the userID; If that replica fails, however, then there has to be a failover that points that user to another replica instead (with the same monotonic read guarantee for that user).

##### Consistent Prefix Reads

Network lags might result in causally-linked payloads arriving out of order.

- E.g. response payloads coming before any request payloads observed to go out

_Consistent Prefix Reads_ guarantees that if a sequence of writes happens in a certain order, then anyone reading those writes will see them appear in the same order.

- Writes that are causally related to each other are written to the same partition
- There are also algorithms that explicitly keep track of causal dependencies (more on this later)

##### Solutions for Replication Lag

If the application is fine with replication lag stretching to minutes or even hours, then you might not need to solve it, you can just favor eventual consistency.

In most cases, that degrades the experience, so you should decide if the system wants to provide a stronger consistency guarantee (e.g. read-after-write).

Database transactions would also be helpful in making sure that commits happen together or not at all.

- Single-node transactions have existed for a long time.
- However, in the move to distributed (replicated and partitioned) databases, many systems have abandoned them, claiming that transactions are too expensive in terms of performance and availability, and asserting that eventual consistency is inevitable in a scalable system.
- That is oversimplified (will return to topic of transactions)

#### Multi-leader replication

Leader-based replication has one major downside: there is only one leader, and all writes must go through it.

If you can't connect to the leader for any reason, you can't write to the database.

A way to address this failure point is the allow for more than one node to accept writes.

- Replication still happens in the same way
- Each node that processes a write must forward that data change to all the other nodes.

This kind of _active/active_ replication involves each leader simultaneous acting as a follower to the other leaders.

##### Use-cases for Multi-Leader Replication

- Multi-datacenter operation
  - If your replicas are physically distributed, then each datacenter can have a local leader which replicates to its local followers
  - Between datacenters, each datacenter's leader replicates its changes to the leaders of other datacenters
  - More performant to distribute write load amongst multiple leaders
  - More tolerant to outage of one datacenter, since other data centers still have leaders and not impacted
  - More tolerant to network faults, since multiple possible locations to route a write to.
- Rarely sensible to use multiple leaders within a single datacenter.
- Multi-leader replication is generally to be regarded with caution, for the same reasons that failover of leaders can go wrong. If multiple sources of truth, important to ensure they do not conflict.

##### Handling write conflicts

In principle, you could make conflict detection synchronous -- i.e., wait for the write to be replicated to all replicas before telling the user that the write was successful.
However, by doing so, you would lose the main advantage of the multi-leader replication: allowing each replica to accept writes independently.
If you want synchronous conflict detection, you might as well just use single leader replication.

Simple way is to avoid conflicts in the first place by mapping a given user to always route toward a particular leader.

If you really want to have a true multi-leader setup, then you need to define convergence policy:

- Last write wins
- Log the conflict and resolve later (programmatically or otherwise)
- Define a particular machine as the winner by default (e.g. robot is the source of truth)

Multi-leader replication should follow a sufficiently dense path so that there is no single point of failure in a replication chain.

Causal writes (e.g. referencing an update that depends on an insert), cannot be achieved with system clock alone, since it's not accurate enough to sync these payloads. You need _version vectors_

#### Leaderless Replication (aka Dynamo-style)

What if we get rid of this idea that only particular nodes can process a write?

Notable examples:

- Dynamo
- Riak
- Cassandra
- Voldemort

Writes need to be sent to all replicas, and the write is accepted if there is quorum.
Reads are also sent to several nodes in parallel, and the read considered valid only if there is quorum.

Version numbers also help with determining which value is more recent.
So the client can write to the lagging node (_read repair_).
You can also have a background anti-entropy process which looks for diffs in data copies between nodes.

##### Quorums on reading and writing

If there are `n` replicas, every write must be confirmed by `w` nodes and every read must be echoed by at least `r` nodes.

As long as `w` + `r` > `n` we expect to get an up-to-date value when reading, because at least one of the `r` nodes we are reading must be up to date.

You typically want an odd `n` so that you can have a tie-breaker.

However there are many valid configurations:

- If you have few writes and many reads, you might benefit from setting `w = n` and `r = 1`
  - Faster reads, but a single failed node causes all database writes to fail.
  - `w < n` gives you write fail redundancy
  - `r < n` gives you read fail redundancy
- Reads and writes are sent to all `n` replicas in parallel. `w` and `r` determine how many responses we wait for.
- You can drop `w` and `r` such that the quorum condition isn't satisfied, then you trade consistency (knowing you read at least one accurate copy by the pidgeonhole principle), in exchange for lower latency / higher availability.
- No widely accepted way right now to quantify staleness of data in leaderless systems
- You basically want a combination of read repair + anti-entropy otherwise you accept possibility of (significant staleness)

Quorums can be _sloppy_, in which the client cannot assemble the `n` nodes it needs for writing, and thus just writes to some collection of "refugee" nodes and allows them to hand along the value when the home nodes of the value come back online (a _hinted handoff_).

- Increases write availability, provides some baseline assurance of durability (data is stored on w nodes somewhere, even though it's not the w nodes of the n home nodes for a given piece of data)
- However, the tradeoff here would be that you have a divergence of your usual quorum condition, and in the meantime you deal with poorer data locality + additional copies of the data on stray nodes

##### Handling concurrent writes in leaderless replications

Suppose you have 3 nodes, each of which receives a different concurrent write. Due to a network distruption, 1 node thinks the value is B and 2 others think the value is A

You need to converge the values or they will just stay inconsistent.

- Last write wins
  - Kind of arbitrary though; the correct write (majority one) might end up dropped
  - The only safe way of using a database with LWW is to ensure that a key is only written once and thereafter treated as immutable, thus avoiding concurrent updates to the same key.
- If you use a UUID as the write key, you can't mutate it, so you can safely use last write wins to deconflict.

You consider writes concurrent if they happened without causal knowledge of each other. They are in contention for the same spot on the causal chain.

### Chapter 6: Partitioning

### Chapter 7: Transactions

### Chapter 8: The Trouble with Distributed Systems

### Chapter 9: Consistency and Consensus

## Part 3: Derived Data

### Chapter 10: Batch Processing

### Chapter 11: Stream Processing

### Chapter 12: Future of Data Systems
