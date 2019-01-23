import matplotlib.pyplot as plt
from pylab import rcParams
from mpl_toolkits.mplot3d import Axes3D
rcParams['figure.figsize'] = 16, 12

x = list()
y = list()
z = list()
u = list()
v = list()
w = list()

file = open('10000.txt', 'r')
lines = file.readlines()
# 0 1 2: pos, 5 6 7: Acoustrophoretic force, 8 9 10: Total force, 11: Radiation potential
for line in lines:
    tmp = list(map(lambda f: float(f), line.split()))
    if tmp[2] > 0.1 and -1e-9 < tmp[10] and tmp[10] < 1e-9:
        x.append(tmp[0])
        y.append(tmp[1])
        z.append(tmp[2])
        u.append(0)
        v.append(0)
        #u.append(tmp[8])
        #v.append(tmp[9])
        w.append(tmp[10])
file.close()

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.quiver(x, y, z, u, v, w,                 # data
          length=4e3,                      # arrow length
          color='Tomato'                    # arrow colour
          )

ax.set_title('3D Vector Field')             # title
ax.view_init(elev=18, azim=30)              # camera elevation and angle
ax.dist=10                                   # camera distance
ax.set_xlim3d(-0.05, 0.2)
ax.set_ylim3d(-0.05, 0.2)
ax.set_zlim3d(0, 0.4)

plt.show()