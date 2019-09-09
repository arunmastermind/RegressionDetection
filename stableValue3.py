import matplotlib.pyplot as plt
import statistics
import numpy as np

def stableSmallest(values, stablePercent):
    stablepoint = 2
    stablepoints = []
    countregression = 0
    countstability = 0
    upperlimit = []
    lowerlimit = []
    stabpts = []
    regressions = []

    plt.style.use('seaborn-whitegrid')
    plt.axis([0, 20, 0, 6])
    # plt.figure()

    for i in range(0, len(values)):
        print(f'------------------------------------\nVALUES: {values[i]}')

        upperlimit.append(stablepoint+1)
        lowerlimit.append(stablepoint-1)

        stabpts.append(stablepoint)
        print(f'UpperLimit: {upperlimit[-1]}\nLowerLimit: {lowerlimit[-1]}')
        if values[i]<=upperlimit[-1] and values[i]>=lowerlimit[-1]:
           stablepoints.append(values[i])
           countstability += 1
           countregression = 0

        else:
            print(stablepoints)
            countregression += 1
            countstability = 0
            stablepoints.clear()

        if values[i] >= upperlimit[-1]:
            regressions.append(values[i])
            plt.plot(i, values[i], 'ro')
            # plt.legend(['Spikes'])
            if countstability >= 3:
                print(f'Regression At {values[i-countstability]}')
                plt.plot(i-countstability, values[i-countstability], 'X', color='red')
            elif countregression >= 3:
                print(f'Regression At {values[i-countregression]}')
                plt.plot(i-countregression, values[i-countregression], 'X', color='red')

        if values[i] <= stablepoint:
            if countstability >= 3:
                print(f'stable values: {stablepoints}')
                if len(stablepoints) > 0:
                    stablepoint = statistics.mean(stablepoints)
                    print(f'NEW KPI {stablepoint}')

    plt.plot(values, color='blue')
    plt.plot(lowerlimit,  color='green')
    plt.plot(upperlimit,  color='green')
    plt.plot(stabpts,  color='red')
    # plt.scatter(regressions, 'ro')

    # plt.legend(['Values','Lower Limit','Upper Limit','KPI'])
    # plt.show()

if __name__ == "__main__":
    stablePercent = 10
    values = [2, 2, 2, 2.1, 2.5, 2.5, 2.5, 2.6, 2.8, 5, 5.5, 5.6, 5.8, 5.9, 1, 1, 1, 0.3, 0.3, 0.2, 0.1]
    stableSmallest(values, stablePercent)
    plt.show()