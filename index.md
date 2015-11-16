##Indexes in MongoDb

Indexes support the efficient resolution of queries. Without indexes, MongoDB must scan every document of a collection to select those documents that match the query statement. This scan is highly inefficient and require the mongodb to process a large volume of data. Indexes are special data structures, that store a small portion of the data, set in an easy to traverse form. The index stores the value of a specific field or set of fields, ordered by the value of the field as specified in index. MongoDb creates index of `_id` attribute by default.

__Index Creation__

`createIndex()` method creates index on a collection. To create an index on a field or fields, we pass to the createIndex() method an index key specification document that lists the fields to index and the index type for each field:

`{ <field1>: <type1>, ...}`

* For an ascending index type, specify 1 for `<type>`.
* For a descending index type, specify -1 for `<type>`.

`db.teams.createIndex({"founded":1})` creates an index on founded attriute.


__Compound Index__

MongoDB supports compound indexes which are indexes on multiple fields. The order of the fields determine how the index stores its keys. For example, the following operation creates a compound index on the "cuisine" field and the "address.zipcode" field. The index orders its entries first by ascending "cuisine" values, and then, within each "cuisine", by descending "address.zipcode" values.

`db.restaurants.createIndex( { "cuisine": 1, "address.zipcode": -1 } )`

__Other useful Index commands__

* getIndexes: `db.teams.getIndexes()` returns all of the indexes of a collection.

* dropIndex: `db.teams.dropIndex({"founded":1})` drops index on founded attribute. 


[Previous](https://github.com/joed7/MongoDb/blob/master/pymongo.md)  |  [Home](https://github.com/joed7/MongoDb/blob/master/home.md)  |  [Next](https://github.com/joed7/MongoDb/blob/master/sharding.md)