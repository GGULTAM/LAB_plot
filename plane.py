import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import rcParams
rcParams['figure.figsize'] = 10, 10

y = list()
z = list()
v = list()

file = open('5000.txt', 'r')
lines = file.readlines()
# 0 1 2: pos, 5 6 7: Acoustrophoretic force, 8 9 10: Total force, 11: Radiation potential
for line in lines:
    tmp = list(map(lambda f: float(f), line.split()))
    if (0.001 < (0.07 - tmp[0]) and (tmp[0] - 0.07) < 0.001):
        y.append(tmp[1] / (0.008575/2))
        z.append(tmp[2])
        v.append(tmp[11])
file.close()

#plt.axes([-0.05, -0.1, 0.25, 0.5])
plt.scatter(y, z, edgecolors='none', s=100, c=v)
plt.legend()
plt.show()