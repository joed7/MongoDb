''' Python script demonstrating delete command in pymongo
'''
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db=connection.nhl
teams = db.teams

def remove(id):
    ''' Delete the team corresponding to _id 31
    '''
    try:
        result = teams.delete_one({'_id':id})
        print "num removed: ", result.deleted_count
    except Exception as e:
        print "Exception: ", type(e), e

remove(31)
