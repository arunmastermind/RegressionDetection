# # Logistic Regression
#
# # Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('logesticRegression.csv')
X = dataset.iloc[:, 1].values
y = dataset.iloc[:, 0].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
fig = plt.figure()
gs = fig.add_gridspec(2,2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, :])

ax3.plot(X,y)
plt.suptitle('Sharing x per column, y per row')
for i in range(0, len(X_train)):
    ax1.plot(X_train[i], y_train[i], '*')
print('\n\n')
for i in range(0, len(X_test)):
    ax2.plot(X_test[i], y_test[i], 'x')

# Fitting Logistic Regression to the Training set
# from sklearn.linear_model import LogisticRegression
# classifier = LogisticRegression(random_state = 0)
# classifier.fit(X_train, y_train)

plt.show()