import os
from itertools import chain
import subprocess
from subprocess import DEVNULL

scalac = "/Users/arunkumar/scala/bin/scalac"

def find_all(basedir, pred):
    for root, dirs, files in os.walk(basedir):
        for fn in files:
            path = os.path.join(root, fn)
            if pred(path):
                yield path

files = chain(
    find_all("/Users/arunkumar/dotty/", lambda p: p.endswith('.scala')),
    find_all("/Users/arunkumar/scala2/", lambda p: p.endswith('.scala')))

added_files = chain(
    find_all("/Users/arunkumar/scalaAnalysis/scalaTrainingData/", lambda p: p.endswith('.scala')))

addedfiles = map(lambda x: os.path.basename(x), added_files)

count1 = 0
count2 = 0
count = 0
for file in files:
    if (os.path.basename(file) in addedfiles):
        continue
    a = subprocess.Popen([scalac, file], stdout=subprocess.PIPE, stderr=DEVNULL)
    b = a.stdout.read()
    c = b.decode("utf-8")
    print(file)
    print(c)
    count += 1
    if c=='':
        os.system(f'cp {file} /Users/arunkumar/scalaAnalysis/scalaTrainingData/scalaPos')
        count1 += 1
    else:
        os.system(f'cp {file} /Users/arunkumar/scalaAnalysis/scalaTrainingData/scalaNeg')
        count2 += 1

print(f'all: {count}')
print(f'compiled: {count1}')
print(f'uncompiled: {count2}')