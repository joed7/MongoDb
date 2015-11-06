#Update

MongoDB's update() methods are used to update document into a collection. The update() method syntax looks like this

`db.COLLECTION_NAME.update(SELECTIOIN_CRITERIA, UPDATE_DATA)`

By default, the update() method updates a single document. To update multiple documents, use the multi option in the update() method. 


* __Set operator__

The query 
`db.teams.update({"name":"new jersey devils"},{"$set":{"conference":"western"}})` updates confrence of team with name "new jersey devils" to western.

The update query either either updates the value(if that field exists in the document) or adds the (field,value) pair if field does not exist.

* __Unset operator__

The unset operator removes the specified field fom the document.

The query ` db.teams.update({"name":"new jersey devils"},{"$unset":{"city":1}})` removes the city attribute for the team "New Jersey devils"


* __Manipulating arrays__ 

  * Push: Extends the array by adding an element to the right. For e.g., `db.teams.update({"name":"new jersey devils"},{"$push":{"stanley cups":2016}})` add the value 2016 on the right of the stanley cups array.
    
  * Pull: Removes the specified value from the array. For e.g., `db.teams.update({"name":"new jersey devils"},{"$pull":{"stanley cups":1995}})` removes the element 1995 from the array.
  
  * Pop: Removes the rightmost element from the array. For e.g., `db.teams.update({"name":"new jersey devils"},{"$pop":{"stanley cups":1}})` removes the last element from the array.
  
  * addToSet: If the element already exists, it does not do anything else it is treated as a push.  For e.g. ` db.teams.update({"name":"new jersey devils"},{"$addToSet":{"stanley cups":1995}})` adds 1995 if does not exist already else it does not do anything.