import kaggle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# huh it's not that much is it?

train = pd.read_csv('train.csv')
train = train.to_numpy().T

b1 = (np.cov(train)[0][0]) / (np.var(train[0]))
b0 = np.average(train[1]) - (b1 * (np.average(train[0])))

x = np.linspace(-10, 100, 100)
y = b1 * x + b0

plt.plot(train[0], train[1], 'ro')

plt.plot(x, y, label=f'y = {b1}x + {b0}', color='b', linewidth=2)

plt.show()

test = pd.read_csv('test.csv')
test = test.to_numpy()

# write error and stuff
