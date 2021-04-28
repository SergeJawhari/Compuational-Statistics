L = float(input("Enter the value of the Poisson parameter. "))

N = 25 # number of probabilities calculated.

import math

P = math.exp(-L)

X = [0] # Horizontal axis
Y = [P] # Vertical axis

for i in range(N):
    if i > 0:
        P = P*(L/i)
        X.append(i)
        Y.append(P)
    print(i,P)

import matplotlib.pyplot as plt

plt.plot(X, Y, 'r+')
plt.show()