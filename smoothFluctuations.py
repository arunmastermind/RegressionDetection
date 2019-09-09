# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
#
# dataset = pd.read_csv('logesticRegression.csv')
# X = dataset.iloc[:, 1].values
# y = dataset.iloc[:, 0].values
#
# smooth_data = pd.rolling_mean(X,5).plot(style='k')
#

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import statistics
randgen = np.random.RandomState(9)
npoints = 1e3
noise = randgen.randn(100)
x = 3 + 2*np.linspace(0, 1, 100) + noise
y = signal.detrend(x)
z = signal.detrend(x) - noise
(signal.detrend(x) - noise).max() < 0.01
plt.plot(noise)
plt.plot(x)
plt.plot(y)
plt.plot(z)
plt.show()