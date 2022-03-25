from matplotlib.mathtext import Error
def lowess(x, y, f, iterations) :
  n = len(x)
  w = 1-np.clip(np.abs((x[:, None] - x[None, :])), 0.0, 1.0)
  y_estimate = np.zeros(n)

  for iteration in range(iterations):
    for i in range(n):
      weights = w[:, i]
      b = np.array([np.sum(weights * y), np.sum(weights * y * x)])
      A = np.array([[np.sum(weights),
                     np.sum(weights * x)],
                    [np.sum(weights * x),
                     np.sum(weights * x * x)]])
      beta = linalg.solve(A, b)
      y_estimate[i] = beta[0] + beta[1] * x[i]
    return y_estimate

n = 300
x = np.linspace(0, 2 * math.pi, n)
y = np.sin(x) + 0.3 * np.random.randn(n)
f = 0.25
iterations = 100000
y_estimate = lowess(x, y, f, iterations)
plt.plot(x, y, "r.")
plt.plot(x, y_estimate, "b-")
