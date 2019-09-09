import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

np.random.seed(42)
values = [2, 2.1, 2.5, 2.6, 2.8, 5, 5.5, 5.6, 1, 1, 1, 0.3, 0.3, 0.2, 0.1]
val = np.array(values)
peaks, _ = find_peaks(val, height=5)
print(peaks)
plt.plot(val)
plt.plot(peaks, val[peaks], "x")
plt.show()
