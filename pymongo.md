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
__Code Examples__

Please refer to [Code Examples](https://github.com/joed7/MongoDb/blob/master/code-examples.md) for code-examples of various operations in pymongo.

[Previous](https://github.com/joed7/MongoDb/blob/master/aggregate.md)  |  [Home](https://github.com/joed7/MongoDb/blob/master/home.md)  |  [Next](https://github.com/joed7/MongoDb/blob/master/index.md)