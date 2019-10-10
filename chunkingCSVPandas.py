import pandas as pd

chunk_size = 100000
batch = 1
for chunk in pd.read_csv('a3.csv', chunksize=chunk_size):
    chunk.to_csv('output_filename'+str(batch)+'.csv', index=False)
    batch += 1