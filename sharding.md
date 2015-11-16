#Sharding

Database systems with large data sets and high throughput applications can challenge the capacity of a single server. Sharding is a method for storing data across multiple machines. MongoDB uses sharding to support deployments with very large data sets and high throughput operations.
Each shard is an independent database, and collectively, the shards make up a single logical database.
 
A typical shard looks like this

![](https://github.com/joed7/MongoDb/blob/master/images/sharded-collection.png)     

Sharding addresses the challenge of scaling to support high throughput and large data sets:

* Sharding reduces the number of operations each shard handles. Each shard processes fewer operations as the cluster grows. As a result, a cluster can increase capacity and throughput horizontally.


* Sharding reduces the amount of data that each server needs to store. Each shard stores less data as the cluster grows.


__Sharding in MongoDB__

This image illustrates sharding architecture in MongoDB

![](https://github.com/joed7/MongoDb/blob/master/images/sharded-cluster-production-architecture.png)

Sharded cluster has the following components: shards, query routers and config servers.

* __Shards__: Shards store the data. To provide high availability and data consistency, in a production sharded cluster, each shard is a replica set. 

* __Query Routers__:  Query router  or mongos instances, interface with client applications and direct operations to the appropriate shard or shards. The query router processes and targets operations to shards and then returns results to the clients. A sharded cluster can contain more than one query router to divide the client request load. A client sends requests to one query router. Most sharded clusters have many query routers.

* __Config servers__: Config servers store the cluster’s metadata. This data contains a mapping of the cluster’s data set to the shards. The query router uses this metadata to target operations to specific shards. Production sharded clusters have exactly 3 config servers.

__Data Partitioning__

MongoDB distributes data, or shards, at the collection level. Sharding partitions a collection’s data by the shard key. To shard a collection, you need to select a shard key. A shard key is either an indexed field or an indexed compound field that exists in every document in the collection. MongoDB divides the shard key values into chunks and distributes the chunks evenly across the shards. To divide the shard key values into chunks, MongoDB uses either range based partitioning or hash based partitioning. See the Shard Key documentation for more information.

* Range Based Sharding: For range-based sharding, MongoDB divides the data set into ranges determined by the shard key values to provide range based partitioning. Consider a numeric shard key: If you visualize a number line that goes from negative infinity to positive infinity, each value of the shard key falls at some point on that line. MongoDB partitions this line into smaller, non-overlapping ranges called chunks where a chunk is range of values from some minimum value to some maximum value.

![](https://github.com/joed7/MongoDb/blob/master/images/sharding-range-based.png)

* Hash Based Sharding: For hash based partitioning, MongoDB computes a hash of a field’s value, and then uses these hashes to create chunks.
With hash based partitioning, two documents with “close” shard key values are unlikely to be part of the same chunk. This ensures a more random distribution of a collection in the cluster.

![](https://github.com/joed7/MongoDb/blob/master/images/sharding-hash-based.png)

[Previous](https://github.com/joed7/MongoDb/blob/master/index.md)  |  [Home](https://github.com/joed7/MongoDb/blob/master/home.md)  |  [Next](https://github.com/joed7/MongoDb/blob/master/code-examples.md)