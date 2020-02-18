import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

i = 0.03
d = 250
p = 1000

l =  [None] * d
for idx in range(d):
    l[idx] = p
    p = p * (1 + i)
    print(p)

fig, ax = plt.subplots()

#ax.semilogy(np.asarray(l)/1000)
#for axis in [ax.yaxis]:
    #axis.set_major_formatter(ScalarFormatter())
plt.plot(np.asarray(l)/1000)
plt.ylabel('k - $')
plt.xlabel('days')
plt.grid(True)
plt.title(str(i*100) + '% per day')
plt.show()