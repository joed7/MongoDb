##PyMongo

PyMongo is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python. It can be installed from either pip or easy_install. In order to use pymongo, we have to do `import pymongo` in our code. 

__Connecting to MongoDB__

The code below opens a connection with the running mongodb instance 

```
import pymongo
connection = pymongo.MongoClient("mongodb://localhost")
```
The above code will connect on the default host and port. We can also specify the host and port explicitly, as follows

```
connection = pymongo.MongoClient('mongodb://localhost:27017/')
```

A single instance of MongoDB can support multiple independent databases. When working with PyMongo we can access databases using attribute style access on MongoClient instances:

```
db = client.test_database
```
Getting a collection in PyMongo works the same as getting a database:

```
collection = db.test_collection
```

__CRUD operations using PyMongo__

* __Create__: [Here](https://github.com/joed7/MongoDb/blob/master/using_insert.py) is an example of data insertion in mongodb.  

* __Read__: [Here](https://github.com/joed7/MongoDb/blob/master/find.py) is example of fetching data from mongodb.

* __Update__: [Here](https://github.com/joed7/MongoDb/blob/master/using_update.py) is an example of updating documents in mongodb.
 
* __Remove__: [Here](https://github.com/joed7/MongoDb/blob/master/using_remove.py) is an example of deleting documents from mongodb.

__Other examples using pymongo__

* [Here](https://github.com/joed7/MongoDb/blob/master/projection_example.py) is an example of projection in pymongo.

* [Here](https://github.com/joed7/MongoDb/blob/master/gt_lt_example.py) is an example of using `$gt` operator in pymongo.

* [Here](https://github.com/joed7/MongoDb/blob/master/limit_skip_sort.py) is an example of using sort, limit in pymongo. 

