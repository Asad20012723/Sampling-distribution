from scipy.stats import binom
import matplotlib.pyplot as plt
# setting the values
# of n and p
n = 100
p = 0.4
# defining list of r values
r_values = list(range(n + 1))
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# plotting the graph 
plt.bar(r_values, dist)
plt.show()