import numpy as np
a = 0.2
b = 0.95e-8
c = -1e-6
d = 0.2

def position(t):
    return np.cos(a*t) + b*t**5 + c*t**4 + d*t

tList = np.linspace(0,100,1001)
xList = position(tList)
data = np.transpose([tList,xList])
np.savetxt("data.dat", data, fmt="%s")