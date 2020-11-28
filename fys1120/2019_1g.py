import numpy as np
import matplotlib.pyplot as plt

L = 5
npoints = 26
a = 2
b = 4
x = np.linspace(-L, L, npoints)
y = np.linspace(-L, L, npoints)
X, Y = np.meshgrid(x, y)
Ex = X.copy()
Ey = X.copy()
for i, ix in enumerate(x):
    for j, iy in enumerate(y):
        r = np.sqrt(ix**2 + iy**2)
        if (r>b):
            Ex[j, i] = 0.0
            Ey[j, i] = 0.0
        elif (r<a):
            E = r/a**3 - r/b**3
            Ex[j, i] = E*ix/r
            Ey[j, i] = E*iy/r
        else:
            E = -r/b**3 + 1/r**2
            Ex[j, i] = E*ix/r
            Ey[j, i] = E*iy/r
plt.quiver(X, Y, Ex, Ey)
plt.show()

