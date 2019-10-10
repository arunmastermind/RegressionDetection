import pandas as pd
import numpy as np
index= [1, 2, 3, 4, 5, 6, 7, 'reg']
df1 = pd.read_csv('output_filename.csv', names=index)
df2 = pd.read_csv('output_filename2.csv', names=index)
df3 = pd.read_csv('output_filename3.csv', names=index)
print(df1.head())
print(df2.head())
print(df3.head())
a = [df1, df2, df3]
finaldf = pd.concat(a)
# finaldf = df1.merge(df2)
print(finaldf.head(10))
print(finaldf.shape)
print(finaldf.size)

finaldf.to_csv("lowerTheBetter.csv", index=False, header=False, encoding='utf8')
