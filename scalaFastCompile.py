import os
import subprocess
from subprocess import DEVNULL

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

n = 10
# print(dir(subprocess))
dir = "/Users/arunkumar/RegressionDetection/fuzzball/results/1/"
scalac = "/Users/arunkumar/scala/bin/scalac"

def test(x):
    a = subprocess.Popen([scalac, x], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    b = a.stderr.read()
    return b

files = os.listdir(dir)
chunk_files = list(divide_chunks(files, n))
for file in chunk_files:
    a = (' '.join(map(lambda x: dir+x, file)))
    k = scalac + ' ' + a
    m = subprocess.Popen([scalac, a], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f'-----------\n{m.stderr.read()}\n---------------\n')


