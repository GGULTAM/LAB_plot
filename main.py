import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 10, 5

plots = list()
plot_z = list()
plot_v = list()

file = open('list_row.txt', 'r')
lines = file.readlines()
for line in lines:
    if line.split()[2] != 'NaN':
        z = float(line.split()[1]) / (0.008575/2)
        v = line.split()[2].split('+')[0]
        if line.split()[2][0] == '-':
            v = '-' + v.split('-')[1]
        else:
            v = v.split('-')[0]
        v = float(v)
        plots.append((z, v))
file.close()

plots.sort()
for p in plots:
    plot_z.append(p[0])
    plot_v.append(p[1])
plt.plot(plot_z, plot_v)
plt.title('yz cut plane at x=7(cm), y=7(cm)')
plt.xlabel('1 grid = λ/2 (λ=8.575mm)')
plt.ylabel('pressure(Pa)')
plt.show()