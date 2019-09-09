import matplotlib.pyplot as plt
import statistics


plt.style.use('seaborn-whitegrid')
plt.axis([0, 10, 0, 6])

def stableSmallest(values, stablePercent):
    stablepoint = 2
    stablepoints = []
    countregression = 0
    countstability = 0
    regressionvalue = 0
    KPI = []
    for i in range(0, len(values)):
        print(f'------------------------------------\nVALUES: {values[i]}')
        upperlimit = stablepoint+1
        lowerlimit = stablepoint-1
        print(f'UpperLimit: {upperlimit}\nLowerLimit: {lowerlimit}')
        if values[i]<=upperlimit and values[i]>=lowerlimit:
           stablepoints.append(values[i])

           countstability += 1
           countregression = 0

        else:
            regressionvalue = i
            print(stablepoints)
            countregression += 1
            countstability = 0
            stablepoints.clear()

        if values[i] >= upperlimit:
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


if __name__ == "__main__":
    stablePercent = 10
    values = [2,2.1, 2.5, 5, 5.5, 5.6, 1, 1, 1, 1, 3]
    stableSmallest(values, stablePercent)