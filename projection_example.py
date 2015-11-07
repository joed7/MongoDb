import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db=connection.nhl
teams = db.teams


def find():

    query = {'division':'central'}
    projection = {'name':1,'city':1,'_id':0}
    
    try:
        cursor = teams.find(query, projection)
    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc


find()
