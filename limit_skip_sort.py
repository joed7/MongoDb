'''Python script demonstraing limit,sort
'''

import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db=connection.nhl
teams = db.teams


def find():

    query = {}
    projection = {'name':1,'_id':0,'founded':1}    

    try:
        cursor = teams.find(query,projection).sort('founded',pymongo.ASCENDING).limit(4)

    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc
        


find()

