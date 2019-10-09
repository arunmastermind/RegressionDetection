import os
from itertools import chain
import shutil
import subprocess
from subprocess import DEVNULL
import re
scalac = "/Users/arunkumar/scala/bin/scalac"

def find_all(basedir, pred):
    for root, dirs, files in os.walk(basedir):
        for fn in files:
            path = os.path.join(root, fn)
            if pred(path):
                yield path

files = chain(
    find_all("/Users/arunkumar/test1/", lambda p: p.endswith('.scala')))

# for i in files:
#     os.system(f'cp {re.escape(i)} /Users/arunkumar/test1/')

added_files = chain(
    find_all("/Users/arunkumar/test/", lambda p: p.endswith('.scala')))

addedfiles = map(lambda x: os.path.basename(x), added_files)

count1 = 0
count2 = 0
count = 0
for file in files:
    # if (os.path.basename(file) in addedfiles):
    #     continue
    a = subprocess.Popen([scalac, file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    b = a.stdout.read()
    x = a.stderr.read()
    c = b.decode("utf-8")
    y = x.decode("utf-8")
    print(f'FILE: {file}')
    print(f'OUTPUT: {c}')
    # print(f'ERROR: {y}')

    q = re.search('errors', c)

    if q is not None:
        os.remove(file)
        print(f'REMOVED {file} !!!!!\n')
    # count += 1
    # if c=='':
    #     os.system(f'cp {file} /Users/arunkumar/scalaExampleFinal/scalaPos')
    #     count1 += 1
    # else:
    #     os.system(f'cp {file} /Users/arunkumar/scalaExampleFinal/scalaNeg')
    #     count2 += 1

print(f'all: {count}')
print(f'compiled: {count1}')
print(f'uncompiled: {count2}')