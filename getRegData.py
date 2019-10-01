import pandas as pd
col_Names=["1", "2", "3", "4", "5", "regression"]
df= pd.read_csv("test.csv", names=col_Names)
def update(value):
    values = value[0:5]
    for j in range(len(values)):
        try:
            if values[j+1] > values[j] and values[j+2] > values[j] and values[j+3] > values[j] and min(values[j+1:]) > values[j]:
                value[7] = 1
            else:
                value[7] = 0
        except:
            continue

    df.to_csv("output_filename.csv", index=False, header=False, encoding='utf8')

for i in range(len(df)):
    update(df.iloc[i].values)
