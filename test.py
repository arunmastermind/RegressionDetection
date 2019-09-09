import os
import subprocess
from subprocess import DEVNULL
import sys
import re
dir = "/Users/arunkumar/RegressionDetection/fuzzball/results/1/"
files = os.listdir(dir)
scalac = "/Users/arunkumar/scala/bin/scalac"
# filename = dir+'test.scala'
count1 = 0
count2 = 0
count = 0
for file in files:
    filename = dir + file
    print(filename)
    a = subprocess.Popen([scalac, filename], stdout=subprocess.PIPE, stderr=DEVNULL)
    print(type(a))
    b = a.stdout.read()
    c = b.decode("utf-8")
    print(c)
    count += 1
    if c=='':
        count1 += 1
    else:
        count2 += 1
#
print(f'all: {count}')
print(f'compiled: {count1}')
print(f'uncompiled: {count2}')

'''
all: 1221
compiled: 25
uncompiled: 1196
'''
