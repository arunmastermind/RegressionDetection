final = []
import numpy as np
import pandas as pd

final.append(np.random.randint(1, 100, size=(1000000,7)))
df = pd.DataFrame(final[0])
df.to_csv("a1.csv", index=False, header=False, encoding='utf8')