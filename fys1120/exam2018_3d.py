import numpy as np
import matplotlib.pyplot as plt

q0 = 0
tau = 3.4
Qinf = 4
dt = 1e-5
time = 10
n = int(np.ceil(time/dt))
Q = np.zeros((n, 1), float)

Q[0] = q0

for i in range(n-1):
    Q[i+1] = Q[i] + (1/tau)*(Qinf - Q[i])*dt

plt.plot(Q)
plt.show()
