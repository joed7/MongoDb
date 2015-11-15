''' Python script demonstrating find command in pymongo
'''
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db=connection.nhl
teams = db.teams


def find():
    '''Return all of the teams in western confence
    '''
    query = {'conference':'western'}

    try:
        cursor = teams.find(query)

    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc
        


def find_one():
    '''Return the team with _id 1
    '''
    query = {'_id':1}
    
    try:
        doc = teams.find_one(query)
        
    except Exception as e:
        print "Unexpected error:", type(e), e

    print doc

find()
#find_one()
