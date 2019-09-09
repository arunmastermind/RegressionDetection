import matplotlib.pyplot as plt
import statistics


plt.style.use('seaborn-whitegrid')
# plt.axis([0, 10, 0, 6])
plt.figure()

def stableSmallest(values, stablePercent):
    stablepoint = 2
    stablepoints = []
    countregression = 0
    countstability = 0
    regressionvalue = 0
    KPI = []
    upperlimit = []
    lowerlimit = []
    plt.plot(values)
    stabpts = []
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
            regressionvalue = i
            print(stablepoints)
            countregression += 1
            countstability = 0
            stablepoints.clear()

        if values[i] >= upperlimit[-1]:
            if countstability >= 3:
                print(f'Regression At {values[i-countstability]}')
            elif countregression >= 3:
                print(f'Regression At {values[i-countregression]}')

        if values[i] <= stablepoint:
            if countstability >= 3:
                print(f'stable values: {stablepoints}')
                if len(stablepoints) > 0:
                    stablepoint = statistics.mean(stablepoints)
                    print(f'NEW KPI {stablepoint}')

    plt.plot(lowerlimit)
    plt.plot(upperlimit)
    plt.plot(stabpts)
    plt.legend(['Values','Lower Limit','Upper Limit','KPI'])
    plt.show()



if __name__ == "__main__":
    stablePercent = 10
    values = [2,2.1, 2.5, 2.6, 2.8, 5, 5.5, 5.6, 1, 1, 1, 0.3, 0.3, 0.2, 0.1]
    stableSmallest(values, stablePercent)
    plt.show()