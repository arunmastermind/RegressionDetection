import pandas as pd
import numpy as np
# col_Names=["1", "2", "3", "4", "5", "regression"]
# df= pd.read_csv("test.csv", names=col_Names)
# df = df.head(10)
def update(value):
    value = value.tolist()
    value.append(0)
    values = value[0:7]
    for j in range(len(values)):
        try:
            if values[j+1] > values[j] and values[j+2] > values[j] and values[j+3] > values[j] and min(values[j+1:]) > values[j]:
                value[7] = 1
                break

            else:
                value[7] = 0
                continue
        except:
            continue
    print(value)
    return value
    # df.to_csv("output_filename.csv", mode='a', index=False, header=False, encoding='utf8')


if __name__ == '__main__':
    a=[]
    # batchNo = 3
    extension = '.csv'
    for batchNo in range(3, 100):
        df = pd.read_csv('output_filename'+str(batchNo)+extension)
        for i in range(len(df)):
            a.append(update(df.iloc[i].values))

        df1 = pd.DataFrame(a)
        df1.to_csv("outputFinal"+str(batchNo)+extension, index=False, header=False, encoding='utf8')

