import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import rcParams
rcParams['figure.figsize'] = 10, 10

x = list()
y = list()
z = list()
v = list()

file = open('5000.txt', 'r')
lines = file.readlines()
# 0 1 2: pos, 5 6 7: Acoustrophoretic force, 8 9 10: Total force, 11: Radiation potential
for line in lines:
    tmp = list(map(lambda f: float(f), line.split()))
    if (0 < tmp[2] and tmp[2] < 0.4):
        x.append(tmp[0])
        y.append(tmp[1])
        z.append(tmp[2])
        v.append(tmp[11])
file.close()

#plt.axes([-0.05, -0.1, 0.25, 0.5])
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_title('Radiation Potential')
ax.view_init(elev=18, azim=30)
ax.dist=10
ax.set_xlim3d(-0.05, 0.2)
ax.set_ylim3d(-0.05, 0.2)
ax.set_zlim3d(0, 0.4)

cmap = plt.cm.get_cmap("hot")
l = ax.scatter(x, y, z, cmap=cmap, c=v, s=20)

fig.colorbar(l)
plt.show()