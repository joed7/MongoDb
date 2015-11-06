#Projection

By default, the find command returns all of the attributes in a document. To filter out specific fields, we can sepcify the fields we want as a document, as a parmeter to find method,  which is called projection.

The query `db.teams.find({"_id":1})` returns

```
{
	"_id" : 1,
	"conference" : "eastern",
	"division" : "atlantic",
	"name" : "boston bruins",
	"city" : "boston, massachusetts, united states",
	"head coach" : "claude julien",
	"home arena" : "td garden",
	"stanley cups" : [
		1929,
		1939,
		1941,
		1970,
		1972,
		2011
	],
	"founded" : 1924,
	"general manager" : "don sweeney"
}
```

If we are interested only in team's name and division, we can use the projection like this
`db.teams.find({"_id":1},{"name":1,"division":1});`, this will print team's name and division along with it's id.  By default, projection always returns the `_id` field, to hide that we specify `"_id":0` in projection document.    

