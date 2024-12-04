import numpy as np
import matplotlib.pyplot as plt
phi_spiral = np.linspace(0, 8 * np.pi, 1000)

k_arch = 1 
r_arch = k_arch * phi_spiral
x_arch = r_arch * np.cos(phi_spiral)
y_arch = r_arch * np.sin(phi_spiral)

phi_sceptre = np.linspace(0.01, 8 * np.pi, 1000)  
k_sceptre = 1  
r_sceptre = k_sceptre / np.sqrt(phi_sceptre)
x_sceptre = r_sceptre * np.cos(phi_sceptre)
y_sceptre = r_sceptre * np.sin(phi_sceptre)

k_rose = 4  
r_rose = np.sin(k_rose * phi_spiral)
x_rose = r_rose * np.cos(phi_spiral)
y_rose = r_rose * np.sin(phi_spiral)

plt.subplot(2, 2, 1)
plt.plot(x_arch, y_arch)
plt.axis('equal')
plt.grid()
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x_sceptre, y_sceptre)
plt.axis('equal')
plt.legend()
plt.grid()

 

plt.subplot(2, 2, 3)
plt.plot(x_rose, y_rose)
plt.axis('equal')
plt.legend()
plt.grid()
plt.savefig('fig_8.png')
 