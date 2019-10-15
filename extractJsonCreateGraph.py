import getScoresFromMongoDB
import pprint
import re
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import argparse

argparser = argparse.ArgumentParser()
# argparser.add_argument('--option', type=str, default="RN_CPUUsage")
argparser.add_argument('--option', type=str)
argparser.add_argument('--bgroup', type=str, default="stashing")
argparser.add_argument('--bname', type=str, default="tradebeans")
argparser.add_argument('--limit', type=int, default=10)
args = argparser.parse_args()

regressions = getScoresFromMongoDB.main(args.bgroup, args.bname, args.limit)
# pprint.pprint(regressions)

def getOptionData(option):
    # print(f'XXXXXXXX {option}')
    y = []
    x = []
    better = ""
    for builds, scores in regressions.items():
        for score in scores:
            pattern = "(.*)"+str(option)+"(.*)"
            if re.search(pattern, str(score.keys())):
                x.append(str(builds))
                y.append(float(list(score.values())[0][0]))
                better = list(score.values())[0][1]
    return (x, y, better)
if args.option:
    plt.style.use('ggplot')
    fig = plt.figure()
    x, y, better = getOptionData(args.option)
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.color'] = 'r'
    plt.xticks(rotation=30)
    plt.yticks(rotation=45)
    plt.xlabel('BUILDS')
    plt.ylabel('SCORES')
    plt.title(f'{args.option} GRAPH with {better}')
    plt.legend(f'{args.option}')
    plt.plot(x, y)
    plt.show()
else:
    plt.style.use('ggplot')
    fig = plt.figure()
    workloadArray = (list(regressions.values())[0])
    # print(workloadArray)
    for i in range(len(workloadArray)):
        workloadDict = (workloadArray[i].keys())
        x = y = []
        better = ''
        for workload in workloadDict:
            print(workload)
            x, y, better = getOptionData(workload)
        print('---------------')

        a = int((len(workloadArray))/2)
        try:
            print(x)
            print(y)
            plt.subplot(a,2,i+1)
            plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=2)
            plt.plot(x,y)
            plt.title(f'{workload} - {better}', fontsize=8)
            plt.xticks(fontsize=5, rotation=70)
            plt.xticks(fontsize=5, rotation=45)
        except:
            continue
    plt.show()
