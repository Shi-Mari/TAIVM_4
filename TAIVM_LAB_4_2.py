import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
z = lambda m: 1.8*np.sqrt(m[0]*m[0]+m[1]*m[1])+1.3*np.cos(np.sqrt(m[0]*m[0]+m[1]*m[1]))+3
dz_dx = lambda m: (-13*m[0]*np.sin(np.sqrt(m[0]*m[0]+m[1]*m[1]))/(10*np.sqrt(m[0]*m[0]+m[1]*m[1]))) + 9*m[0]/(5*np.sqrt(m[0]*m[0]+m[1]*m[1]))
dz_dy = lambda m: (-13*m[1]*np.sin(np.sqrt(m[0]*m[0]+m[1]*m[1]))/(10*np.sqrt(m[0]*m[0]+m[1]*m[1]))) + 9*m[1]/(5*np.sqrt(m[0]*m[0]+m[1]*m[1]))
e = 0.001
a = 0.1
i = 0
M1 = [2.5, 2.5]
X_ar = []
Y_ar = []
while True:
    z0 = z(M1)
    M1[0] = M1[0] - a*dz_dx(M1)
    X_ar.append(M1[0])
    Y_ar.append(M1[1])
    i += 1
    M1[1] = M1[1] - a*dz_dy(M1)
    X_ar.append(M1[0])
    Y_ar.append(M1[1])
    i += 1
    dif = z0 - z(M1)
    if(dif < e):
        break;
print(i, "; ", M1, "; ", z(M1))
X,Y = np.meshgrid(np.arange(-3, 3, 0.01),np.arange(-3, 3, 0.01))
Z = 1.8*np.sqrt(X*X + Y*Y) + 1.3*np.cos(np.sqrt(X*X + Y*Y)) + 3
plt.clabel(plt.contour(X,Y,Z))
plt.plot(X_ar,Y_ar)
plt.scatter(X_ar,Y_ar,s=3)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
