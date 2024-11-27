import numpy as np
import matplotlib.pyplot as plt
phi = np.linspace(0,2*np.pi, 100)
k = 1
r = k * np.sin(phi)
x = r * np.cos(phi)
y = r * np.sin(phi)
plt.figure(figsize=(8,8))
plt.plot(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.savefig('fig_8.png')
plt.axis('equal')