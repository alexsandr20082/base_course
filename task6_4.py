import matplotlib.pyplot as plt
import numpy as np
b = 0.2
k = 1
phi = np.linspace(0,8 * np.pi, 1000)

r_log = np.exp(b * phi)
x_log = r_log * np.cos(phi)
y_log = r_log * np.sin(phi)

r_arhimed = k * phi
x_arhimed = r_arhimed * np.cos(phi)
y_arhimed = r_arhimed * np.sin(phi)

phi_jei = np.linspace(0.01, 8 * np.pi, 1000)
r_jei = k / np.sqrt(phi_jei)
x_jei = r_jei * np.cos(phi)
y_arhimed = r_jei * np.sin(phi_jei)

k_rose = 20
r_rose = np.sin
plt.legend()
plt.savefig('fig_8.png')

