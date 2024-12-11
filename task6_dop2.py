import numpy as np
import matplotlib.pyplot as plt

def plot_ellipse(epsilon, p):
    if not (0 <= epsilon < 1):
        raise ValueError("Экстремаситет должен быть в диапазоне [0, 1)")
    
    phi = np.linspace(0, 2 * np.pi, 1000)

    r = p / (1 + epsilon * np.cos(phi))
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label=f'Эллипс: ε={epsilon}, p={p}')
    plt.title('График эллипса в полярной системе координат')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')  
    plt.grid()
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.legend()
    plt.show()
    plt.savefig('fig_12.png')
