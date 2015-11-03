##Insert Operations


In MongoDB, the `db.collection.insert()` method adds new documents into a collection. Here is an example which insert a team in the database,

```
db.teams.insert(
    {
"conference": "western", 
"division": "central", 
"name": "LA lakers",
 "city": "LA, California", 
 "head coach": "joel quenneville", 
 "home arena": "united center", 
 "stanley cups": ["2009","2010"], 
 "founded": "1926", 
 "general manager": "stan bowman", 
 "_id": "31"
    }
)
```
The operation returns a WriteResult object with the status of the operation. A successful insert of the document returns the following object:
```
WriteResult({ "nInserted" : 1 })
```

One thing to notice here is `_id` field of the document. It serves as the primary key for the collection, If a client inserts a document that does not contain the _id field, MongoDB adds the field with the value set to a generated ObjectId.

__Insert Multiple Documents__

In the previous exmaple, we inserted one document in the collection. We can pass an array of documents to `db.collection.insert()` to insert multiple documents at once.

```
db.teams.insert([
    { 
    "conference": "western", 
    "division": "central",
    "name": "chicago blackhawks", 
    "city": "chicago, illinois", 
    "head coach": "joel quenneville",
    "home arena": "united center", 
    "stanley cups": ["1934", "1938", "1961", "2010", "2013", "2015"], 
    "founded": "1926", 
    "general manager": "stan bowman", 
    "_id": "24"
    }, 
    {
    "conference": "western", 
    "division": "central", 
    "name": "colorado avalanche", 
    "city": "denver, colorado", 
    "head coach": "patrick roy", 
    "home arena": "pepsi center", 
    "stanley cups": ["1996", "2001"], 
    "founded": "1972", 
    "general manager": "joe sakic", 
    "_id": "25"
    }
])    
```