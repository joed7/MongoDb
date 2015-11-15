'''Python script demonstrating comparison operators
'''
import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.nhl
teams = db.teams


def find():

    query = {'stanley cups':{'$gte':2009}}
    projection = {'name':1,'_id':0}    

    try:
        cursor = teams.find(query,projection)

    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc
        

find()

