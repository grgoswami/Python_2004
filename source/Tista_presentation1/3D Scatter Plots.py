from mpl_toolkits.mplot3d import Axes3D 

import matplotlib.pyplot as plt
import numpy as np


np.random.seed(4479306)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


def plot(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

n = 100
color = ''

for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    xs = plot(n, 23, 32)
    ys = plot(n, 0, 100)
    zs = plot(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, marker= 'X', c= color)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()