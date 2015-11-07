import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db=connection.nhl
teams = db.teams

def find():

    query = {'_id':31}
    
    try:
        doc = teams.find_one(query)
        
    except Exception as e:
        print "Unexpected error:", type(e), e

    print doc



def update():


    try:
        teams.update({'_id':31},{'$set':{'conference':'western'}})

    except Exception as e:
        print "Unexpected error:", type(e), e
   
find()
update()
find()   
