import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db=connection.nhl
teams = db.teams


def find():

    query = {'conference':'western'}

    try:
        cursor = teams.find(query)

    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc
        


def find_one():

    query = {'_id':1}
    
    try:
        doc = teams.find_one(query)
        
    except Exception as e:
        print "Unexpected error:", type(e), e

    print doc



find()
#find_one()
