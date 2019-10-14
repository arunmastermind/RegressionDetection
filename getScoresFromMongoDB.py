from pymongo import MongoClient
import argparse
import pprint
from bson.objectid import ObjectId
import re
'''
client = MongoClient('mongodb://qaubd1:27017')
db = client.prf
collection = db.builds
a = collection.find().limit(1)
for i in a:
   print(i)
'''

def getMongodb():
    client = MongoClient('mongodb://qaubd1:27017')
    db = client.prf
    return db

def getMongoConnections(connection):
    db = getMongodb()
    conn = ''
    if connection == 'builds':
        conn = db.builds
    elif connection == 'benchmarks':
        conn = db.benchmarks
    elif connection == 'results':
        conn = db.results

    return conn

def getBuilds(buildId):
    conn = getMongoConnections('builds')
    results = conn.find({'_id': buildId, 'name': {'$regex': '(?i)(.*)dev(.*)'}}, {'name': 1}).limit(1)
    return results

def getBmarkID(bgroup, bname):
    conn = getMongoConnections('benchmarks')
    results = conn.find({'bmark_group': {'$regex': '(?i)(.*)' + (bgroup) + '(.*)'},
                         'bmark_name': {'$regex': '(?i)(.*)' + (bname) + '(.*)'}},
                        {'_id': 1, 'bmark_group': 1, 'bmark_name': 1})
    return results

def getResult(bmarkId, limit):
    conn = getMongoConnections('results')
    results = conn.find({'bmark_id': bmarkId}).limit(limit)
    return results

if __name__ == '__main__':
    regresions = {}
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--bgroup', type=str, default="stashing")
    argparser.add_argument('--bname', type=str, default="tradebeans")
    argparser.add_argument('--limit', type=int, default=20)
    args = argparser.parse_args()

    bmarkId = getBmarkID(args.bgroup, args.bname)
    for id in bmarkId:
        results = getResult(id['_id'], args.limit)
        for result in results:
            buildresult = []
            buildName =''
            build = getBuilds(result['build_id'])
            for buildN in build:
                for i, j in result['results'].items():
                    buildresult.append({i:j})
                    buildName = buildN["name"]
            regresions[buildName] = (buildresult)

    pprint.pprint(regresions)






