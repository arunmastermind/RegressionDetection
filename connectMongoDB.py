from pymongo import MongoClient
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

def getBeanchmarks():
    conn = getMongoConnections('benchmarks')
    # results = conn.find({}, {'id': 1, 'bmark_group': 1, 'bmark_name': 1})
    results = conn.find().sort([('bmark_group', -1)]).limit(2)
    # results = conn.find()
    return results

def getBuilds():
    conn = getMongoConnections('builds')
    # results = conn.find({},{'_id': 1, 'name': 1})
    results = conn.find().sort([('name', -1)]).limit(2)
    return results

if __name__ == '__main__':
    # benchmarks = getBeanchmarks()
    # for benchmark in benchmarks:
    #     print(benchmark)

    # builds = getBuilds()
    # for build in builds:
    #     print(build)

    # countbenchmrk = 0
    # countbuild = 0
    # builds = getBuilds()
    # for build in builds:
    #     countbuild += 1
    #     benchmarks = getBeanchmarks()
    #     for benchmark in benchmarks:
    #         countbenchmrk += 1
    #         # print(f'{countbuild} - {countbenchmrk}: {build["name"]} | {benchmark["bmark_name"]}')
    #         print(f'{countbuild} - {countbenchmrk}: {build["name"]}={build["_id"]} | {benchmark["bmark_name"]}={benchmark["_id"]}')

    conn1 = getMongoConnections('results')
    conn2 = getMongoConnections('builds')
    results = conn1.find( { "bmark_id":ObjectId("5b2274ce4fbd0333c3cb1b47") } )
    build = 0
    build = []
    score = []
    for result in results:
        for x in conn2.find({"_id": ObjectId(result['build_id'])}):

            try:
                build_no = x['name'].split('-')[2]
                if len(build_no) == 4:
                    # print(f'{result["_id"]} - {result["results"]["RN_loop_results_warmup_time"]}')
                    # print(build_no)
                    score.append(result["results"]["RN_loop_results_warmup_time"][0])
                    build.append(build_no)
                else:
                    continue
            except:
                pass





