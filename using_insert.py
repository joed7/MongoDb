
import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")
db=connection.nhl
teams = db.teams


def insert():



    vegas ={"_id":31,"name":"Vegas Hustlers", "city":"Las Vegas, NV",
              "stanley cups":[]}    


    try:
        teams.insert_one(vegas)

    except Exception as e:
        print "Unexpected error:", type(e), e
   
    find(31)

def find(id):

    query = {'_id':id}

    try:
        cursor = teams.find(query)

    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc
        

insert()

