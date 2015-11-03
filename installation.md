##Installation

Refer to the [documentation](https://docs.mongodb.org/manual/installation/) for installation instructions for various operating systems.


__Mongo Shell__

The mongo shell is an interactive JavaScript interface to MongoDB and is a component of the MongoDB package. We can use the mongo shell to query and update data as well as perform administrative operations. Upon installing and launching MongoDB, we can connect to mongo shell by typing `mongo` in terminal.


__Importing Data-Set in MongoDB__

There are various methods of inserting data into MongoDB. We can either insert data using insert command in mongo shell or we can use `mongoimport` command to insert a bunch of collections. The data-set for this presentation is [NHL teams](https://github.com/joed7/MongoDb/blob/master/team.json), it can be imported in mongoDB using the command

```
mongoimport --db nhl --collection teams --drop --file team.json
```
The above command inserts data in `teams` collections in nhl database, dropping the existing collection. In order to access the above collections, We have to

* Connect to mongo shell :`mongo`.    
* Select the appropriate database : `use nhl` 
* Run the mongodb command: `db.teams.findOne()` #returns the first document of the collection
  
`help` command can be used to view the help menu of mongo shell.