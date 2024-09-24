# System Design Cheatsheet

<!--toc:start-->

- [System Design Cheatsheet](#system-design-cheatsheet)
  - [Goals of system design](#goals-of-system-design)
    - [Scalability](#scalability)
    - [Reliability](#reliability)
    - [Availability](#availability)
    - [Efficiency](#efficiency)
    - [Serviceability / Manageability](#serviceability-manageability)
  - [What is Consistent Hashing, and how is it used?](#what-is-consistent-hashing-and-how-is-it-used)
  - [What is Raft, and how is it used?](#what-is-raft-and-how-is-it-used)
  <!--toc:end-->

## Goals of system design

### Scalability

Can the system grow well to meet increased load?

- Load balancer >> make sure load is distributed well across all deployed replicas
  - DNS routing-based load balancing
    - DNS server has one or more A records, each pointing to a different IP address
    - Client accesses some service instance based on the IP address that the DNS server decides to respond with
    - Load balancing algorithms:
      - Round robin (+ weighted variation)
      - Routing to server that is currently serving lowest traffic
      - Routing to server with fewest number of connections
      - Routing randomly
    - In the event of stateful (usually session-based), the routing layer would need some kind of lookup functionality to keep track of which session Ids should be routed back to which server instances
    - What if node, which is managing stateful logic, goes down, then?
      - Important to have backup replica ready to take over
      - Master / slave architecture
      - Likely helpful to have the service write payloads to an event stream, so that if a service goes down, the backup replica can recompute any state that a given session ID is going to have
- Health checks as a way to know which services to route toward
  - Peer-to-peer health checking is generally more interesting, because a centralized health check server represents a single point of failure
- Reverse proxy >> from the perspective of other server components, we are just hitting one and the same point
- DNS routing
  - What is Level 4 vs. Level 7 routing?
- Horizontal vs. Vertical Scaling
  - Horizontal scaling: increase the number of a certain kind of node on the network
    - This is relatively easy to do with container orchestration tooling.
    - What is the Kubernetes API that allows you to achieve this?
      - Horizontal Pod Autoscaler (HPA)
        - Create a HorizontalPodAutoScaler resource, specifying the target resource to scale (like a Deployment), the minimum and maximum number of replicas, and the metrics to use for scaling decisions
        - Common scaling metrics:
          - CPU utilization (most common metric). Average CPU usage across all pods controlled by the scaled resource
          - Memory utilization: Similar to CPU but based on memory usage.
          - Custom app specific metrics:
            - Number of requests per second
            - Queue length
            - Response time
          - External metrics: platform provided metrics that reference an external resource
            - Number of messages in a cloud messaging queue
            - Metrics from a cloud load balancer
          - Object Metrics: These refer to a single Kubernetes object, like the length of a specific queue
          - Pod Metrics
          - Kubernetes Resource metrics (metrics-server, pertaining to the cluster)
  - Vertical scaling: increase the compute resources provisioned for a particular kind of node on the network
    - This usually involves downtime, so it's not something you want to reach for too much

Tradeoffs about Scalability == tradeoffs about resourcing. The main cost is that it is hard to structure stateful dataflows in ways can be independently parallelized

### Reliability

Can the system survive component failures?

- If a user has added an item to their shopping cart, the system is expected not to lose it.
- Redundancy of software components (services), as well as redundancy of data (replications)
- Tradeoffs about reliability == tradeoffs about redundancy. Provisioning for redundancy definitely carries costs; A lot of the obvious cost is money, but a further dimension of cost comes in the form of complexity

### Availability

- Reliability over time

### Efficiency

### Serviceability / Manageability

## What is Consistent Hashing, and how is it used?

## What is Raft, and how is it used?
