##Deletion

In MongoDB, the `db.collection.remove()` method removes documents from a collection. Depending on the query, we can remove all documents from a collection, remove all documents that match a condition, or limit the operation to remove just a single document.


__Remove all documents__

If we pass an empty query document {} to the remove() method, it deletes all the documents of the collection.

```
db.teams.remove({}) #empties the team collection
```


__Remove Documents that Match a Condition__

We can specify a query parmeter to remove method, which deletes only those documents that match that criterion.

```
db.teams.remove({"division":"metropolitan"}) #deletes all of teams that belong to the metropolitan division.
``` 

If we want to remove a single document, we can call the remove() method with the justOne parameter set to true or 1.

```
db.teams.remove({"division":"metropolitan"},1) #deletes one team of all the teams that belong to the metropolitan division.
```

[Previous](https://github.com/joed7/MongoDb/blob/master/update.md)  |  [Home](https://github.com/joed7/MongoDb/blob/master/home.md)  |  [Next](https://github.com/joed7/MongoDb/blob/master/projection.md)