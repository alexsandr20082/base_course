import matplotlib.pyplot as plt
import numpy as np
A = 1
B = 1
d = 0.5
phi=np.linspace(0,2 * np.pi, 1000)

x = A * np.sin(phi + d)
y = B * np.sin(phi)

plt.figure(figsize=(8,6))
plt.plot(x,y)
plt.axis("equal")
plt.grid()

d_values=[0.5,0.025,1.2]
for d in d_values:
    x = A * np.sin(phi + d * np.pi)
    y = B * np.sin(phi)
    plt.plot(x,y,label=d)
    
plt.legend()
plt.savefig('fig_9.png')