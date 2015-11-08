''' Python script demonstrating update command in pymongo
'''
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db=connection.nhl
teams = db.teams

def find():
    ''' Returns the team corresponding to _id 31
    '''
    query = {'_id':31}

    try:
        doc = teams.find_one(query)
    except Exception as e:
        print "Unexpected error:", type(e), e

    print doc

def update():
    '''Setting the conference attribute for the team with _id 31
    '''
    try:
        teams.update({'_id':31},{'$set':{'conference':'western'}})
    except Exception as e:
        print "Unexpected error:", type(e), e
   
find()
update()
find()   
