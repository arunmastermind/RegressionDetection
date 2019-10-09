final = []
import numpy as np
import pandas as pd

final.append(np.random.randint(1000, 100000, size=(10000000,7)))
df = pd.DataFrame(final[0])
df.to_csv("a3.csv", index=False, header=False, encoding='utf8')