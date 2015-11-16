##Aggregation

Aggregations are operations that process data records and return computed results. MongoDB provides a rich set of aggregation operations that examine and perform calculations on the data sets.MongoDB provides aggregation framework, modeled on the concept of data processing pipelines. Documents enter a multi-stage pipeline that transforms the documents into an aggregated result.

The most basic pipeline stages provide filters that operate like queries and document transformations that modify the form of the output document.Other pipeline operations provide tools for grouping and sorting documents by specific field or fields as well as tools for aggregating the contents of arrays, including arrays of documents. In addition, pipeline stages can use operators for tasks such as calculating the average or concatenating a string. 

Here is an exmaple of a very basic match/group pipelines

![](https://github.com/joed7/MongoDb/blob/master/images/aggregation-pipeline.png)

Possible stages in aggregation framework are following:

* `$project`: Used to select some specific fields from a collection.  
* `$match`: This is a filtering operation and thus this can reduce the amount of documents that are given as input to the next stage.  
* `$group`: This does the actual aggregation.  
* `$sort`: Sorts the documents.  
* `$skip`: With this it is possible to skip forward in the list of documents for a given amount of documents.  
* `$limit`: This limits the amount of documents to look at by the given number starting from the current position.  
* `$unwind`: This is used to unwind document that are using arrays. when using an array the data is kind of pre-joinded and this operation will be undone with this to have individual documents again. Thus with this stage we will increase the amount of documents for the next stage.  


__Aggregation Examples__

* `db.teams.aggregate([{"$match":{"conference":"eastern"}},{"$group":{"_id":"$division","count":{"$sum":1}}}])`

The query above returns count of teams in each division in eastern confrence. 

* `db.teams.aggregate([{"$unwind":"$stanley cups"},{"$group":{"_id":"$name","last":{"$max":"$stanley cups"},"first":{"$min":"$stanley cups"}    }}])`

The above query returns the year of the first and most recent cup victory for every team.

* `db.teams.aggregate([{"$group":{"_id":"$division",teams:{"$push":"$name"}}}])`

The query puts the names of all of teams of a division in teams array for every division.

* `db.teams.aggregate([{"$sort":{"founded":1}},{$project:{"_id":0,"team":{$toUpper:"$name"},"founded":1}}])`

This query sorts all of the team by their founded year in increasing order and then selects only team and founded attributes in  the final output.


[Previous](https://github.com/joed7/MongoDb/blob/master/projection.md)  |  [Home](https://github.com/joed7/MongoDb/blob/master/home.md)  |  [Next](https://github.com/joed7/MongoDb/blob/master/pymongo.md)