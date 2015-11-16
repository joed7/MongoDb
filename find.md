##Querying

In MongoDB, the db.collection.find() method retrieves documents from a collection. The db.collection.find() method returns a cursor to the retrieved documents.

__Select All Documents in a Collection__

Giving empty query document `{}` to find method return all documents in the collection. 

```
db.teams.find({}) #return all the documetns in teams collection
```

Doing it is same as leaving query parameter i.e. `db.teams.find()` is same as `db.teams.find({})`


__Specify Equality Condition__

To specify equality condition, we use the query document `{ <field>: <value> }`; it select all documents that contain the `<field>` with the specified `<value>`. 

```
db.teams.find({"division":"pacific"}) #returns the teams of pacific division
```

We can specify multiple `{ <field>: <value> }` paris in the query parameter, MongoDB treats it as and condition on all of the parameters.

```
db.teams.find({"division":"central","conference":"western"}) #returns the teams of central division and western confrence
```

__Specify Conditions Using Query Operators__

We can use query operators to specify query conditions in a MongoDB query.

* __$gt__, __$lt__ operators 

We can specify range queries usng `$gt`, `$lt`,`gte`,`lte` operators, they mean greater than, less than, greater than or equal, less than or equal respectively.

```
db.teams.find({"_id":{"$gte":15}}) #returns all of the docement with _id >= 15
``` 

* __in__ operator

Similar to relational databases, with in operator we can specify the equal condition on multiple values.

```
db.teams.find( { "division": { $in: [ 'central', 'pacific' ] } } ) #returns the teams of central division or pacific division
```

* __and__ and __or__ operator   

As discussed above, `and` operation can be performed by specifying multiple parameters in the query.

Using the $or operator, we can specify a compound query that joins each clause with a logical OR conjunction so that the query selects the documents in the collection that match at least one condition.

```
db.teams.find({ "$or" : [ {"division":"metropolitan"},{"conference":"western"} ] }) #return the teams of metropolitan division or western confrence
```

__Equality Match on Fields within an Embedded Document__

We can use the dot notation to match by specific fields in an embedded document, It will select documents in the collection where the embedded document contains the specified fields with the specified values. 

Consider this example restaurant

```
{
	"_id" : ObjectId("563cfd02cd6cb6dbad46a21e"),
	"address" : {
		"building" : "1007",
		"coord" : [
			-73.856077,
			40.848447
		],
		"street" : "Morris Park Ave",
		"zipcode" : "10462"
	},
	"borough" : "Bronx",
	"cuisine" : "Bakery",
	"name" : "Morris Park Bake Shop",
	"restaurant_id" : "30075445"
}
```
To return the above mentioned restaurant via zipcode, we can run the query `db.house.find({"address.building":"1007"})`.


__Querying Arrays__

* Exact Match on Array

To specify equality match on an array, we use the query document `{ <field>: <value> }` where `<value>` is the array to match. Equality matches on the array require that the array field match exactly the specified `<value>`, including the element order.

For the document in inventory collections,

```
{ _id: 5, type: "food", item: "aaa", ratings: [ 5, 8, 9 ] }
{ _id: 6, type: "food", item: "bbb", ratings: [ 5, 9 ] }
{ _id: 7, type: "food", item: "ccc", ratings: [ 9, 5, 8 ] }
```
If we do `db.inventory.find( { ratings: [ 5, 8, 9 ] } )`, we get `{ "_id" : 5, "type" : "food", "item" : "aaa", "ratings" : [ 5, 8, 9 ] }`

* Match at least one element

If we specify a single element in the array to match, it returns the documents with array which contains at least one element with the specified value.

The query `db.inventory.find( { ratings: 5 } )` on the above inventory collection, returns all documents where ratings is an array that contains 5 as one of its elements.

```
Output
{ "_id" : 5, "type" : "food", "item" : "aaa", "ratings" : [ 5, 8, 9 ] }
{ "_id" : 6, "type" : "food", "item" : "bbb", "ratings" : [ 5, 9 ] }
{ "_id" : 7, "type" : "food", "item" : "ccc", "ratings" : [ 9, 5, 8 ] }
```


__ElemMatch operator__

`$elemMatch` operator specifies multiple criteria on the elements of an array such that at least one array element satisfies all the specified criteria.

For e.g., On the inventory collections, if we run this query `db.inventory.find( { ratings: { $elemMatch: { $gt: 5, $lt: 9 } } } )`, it returns these documents

```
{ "_id" : 5, "type" : "food", "item" : "aaa", "ratings" : [ 5, 8, 9 ] }
{ "_id" : 7, "type" : "food", "item" : "ccc", "ratings" : [ 9, 5, 8 ] }

```
becuase, both of these documents have 8 as ratings which satisfies the search criterion.

If we had ran the above query without the `elemMatch` operator `db.inventory.find( { ratings: { $gt: 5, $lt: 9 } } )`, it would have returned the documents where rating array contains elements that in some combination satisfy the query conditions; e.g., one element can satisfy the greater than 5 condition and another element can satisfy the less than 9 condition, or a single element can satisfy both.

```
Output
{ "_id" : 5, "type" : "food", "item" : "aaa", "ratings" : [ 5, 8, 9 ] }
{ "_id" : 6, "type" : "food", "item" : "bbb", "ratings" : [ 5, 9 ] }
{ "_id" : 7, "type" : "food", "item" : "ccc", "ratings" : [ 9, 5, 8 ] }
```

The document with the `"ratings" : [ 5, 9 ]` matches the query since the element 9 is greater than 5 (the first condition) and the element 5 is less than 9 (the second condition). 

__Querying Array of embedded documents__

Consider the collections

```
{
  _id: 100,
  type: "food",
  item: "xyz",
  qty: 25,
  price: 2.5,
  ratings: [ 5, 8, 9 ],
  memos: [ { memo: "on time", by: "shipping" }, { memo: "approved", by: "billing" } ]
}

{
  _id: 101,
  type: "fruit",
  item: "jkl",
  qty: 10,
  price: 4.25,
  ratings: [ 5, 9 ],
  memos: [ { memo: "on time", by: "payment" }, { memo: "delayed", by: "shipping" } ]
}
```
 
* The query `db.inventory.find( { 'memos.by': 'shipping' } )` returns all documents where the memos field contains an array that contains at least one embedded document that contains the field by with the value 'shipping':

* If we have multiple search criterion, we can use `$elemMatch` operator to return the documents which have at least one embedded document which satisfies all the criteria.

The query below queries for documents where the memos array has at least one embedded document that contains both the field memo equal to 'on time' and the field by equal to 'shipping':
```
db.inventory.find(
   {
     memos:
       {
          $elemMatch:
            {
               memo: 'on time',
               by: 'shipping'
            }
       }
    }
)
```

[Previous](https://github.com/joed7/MongoDb/blob/master/installation.md)  |  [Home](https://github.com/joed7/MongoDb/blob/master/home.md)  |  [Next](https://github.com/joed7/MongoDb/blob/master/insert.md)