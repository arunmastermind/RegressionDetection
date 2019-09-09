import concurrent.futures
import os
import subprocess
from subprocess import DEVNULL
from itertools import chain

dir = "/Users/arunkumar/scala/bin/test/"
files = os.listdir(dir)
scalac = "/Users/arunkumar/scala/bin/scalac"
# filename = dir+'test.scala'
count1 = 0
count2 = 0
count = 0

def find_all(basedir, pred):
    for root, dirs, files in os.walk(basedir):
        for fn in files:
            path = os.path.join(root, fn)
            if pred(path):
                yield path

files = chain(
    find_all("/Users/arunkumar/dotty/", lambda p: p.endswith('.scala')),
    find_all("/Users/arunkumar/scala2/", lambda p: p.endswith('.scala')))
a = 0
for file in files:
    a += 1
    print(file)
print(a)
# def procedure(file):
#     filename = dir+file
#     a = subprocess.Popen([scalac, filename], stdout=subprocess.PIPE, stderr=DEVNULL)
#     b = a.stdout.read()
#     c = b.decode("utf-8")
#     print(c)
#
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     for i in executor.map(procedure, files):
#         print(i)
