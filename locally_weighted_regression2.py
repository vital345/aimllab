import numpy as np
import math
import matplotlib.pyplot as plt

def lowess(x0, X, y, tau):
    # merge row wise
    x0 = np.r_[1, x0]
    # merge column wise
    X = np.c_[np.ones(len(X)), X]
    
    xw = X.T * radial_kernel(x0, X, tau)
    # @ --> matrix multiplication
    # pinv means taking matrix inverse
    beta = np.linalg.pinv(xw @ X) @ xw @ y
    
    return x0 @ beta

def radial_kernel(x0, X, tau):
    return np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau * tau))

n = 300
tau = 0.24

X = np.linspace(0, 2 * math.pi, n)
y = np.sin(X) + 0.3 * np.random.randn(300)
y_predict = [lowess(x0, X, y, tau) for x0 in X]

plt.plot(X, y, "r.") # r. means red coloured dots
plt.plot(X, y_predict, "b-") # b- means blue coloured line
