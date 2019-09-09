# Workload: JniCallBenchmark.tryU64/Score_avgt ( Build range: 2720-; Benchmark: Falcon_jniJMH; )
from pymongo import MongoClient
from bson.objectid import ObjectId
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')

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
    return results

def getBuilds():
    conn = getMongoConnections('builds')
    # results = conn.find({},{'_id': 1, 'name': 1})
    results = conn.find().sort([('name', -1)]).limit(2)
    return results

def toCsv(build, score):
    # importing pandas as pd
    import pandas as pd

    # dictionary of lists
    dict = {'build': build, 'score': score}

    df = pd.DataFrame(dict)

    # saving the dataframe
    df.to_csv('test.csv', header=False, index=False)

if __name__ == '__main__':
    plt.style.use('seaborn-whitegrid')

    conn1 = getMongoConnections('results')
    conn2 = getMongoConnections('builds')
    results = conn1.find({"bmark_id": ObjectId("585566e221c98e7d97606994")})
    # for i in results:
    #     print(i)
    build = []
    score = []
    for result in results:
        for x in conn2.find({"_id": ObjectId(result['build_id'])}):
            # print(x)
            try:
                build_no = x['name'].split('-')[2]
                if len(build_no) == 4:
                    score.append(float(result["results"]["Score_avgt"][0]))
                    build.append(float(build_no))
                else:
                    continue
            except:
                pass
print(build)
print(score)
toCsv(build, score)
plt.xticks(np.arange(0, float(max(build))+5, 5), rotation=70)
plt.yticks(np.arange(0, float(max(score)), 10))

plt.plot(build, score)
plt.show()

