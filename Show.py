import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np



def ParseZ():
    data = []
    with open("dataProj.txt") as f:
        for line in f:
            data.append([float(x) for x in line.split()])
    return data

mtGridSize = int(100)
T = 20
tau = T/mtGridSize

mlGridSize = int(100)
l = 1
h = l/mtGridSize

z = ParseZ()
t = np.zeros((mtGridSize,mlGridSize))
x = np.zeros((mtGridSize,mlGridSize))
y = np.zeros((mtGridSize,mlGridSize))
for i in range(0,mtGridSize):
    for j in range(0,mlGridSize):
        t[i][j] = z[i][j]
        x[i][j] = j*h
        y[i][j] = i*tau

fig = pylab.figure()
axes = Axes3D(fig)
axes.plot_surface(x, y, t)
pylab.show()