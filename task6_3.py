import numpy as np
import matplotlib.pyplot as plt

def plot_ellipse(x_min, x_max, N):
    a = 5 
    b = 3
    x = np.linspace(x_min, x_max, N)
    y_positive = b * np.sqrt(1 - (x**2) / (a**2))
    y_negative = -b * np.sqrt(1 - (x**2) / (a**2)) 
    
    plt.plot(x, y_positive, color='black')
    plt.plot(x, y_negative, color='black')
    plt.title('График эллипса')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.legend()
    plt.savefig('fig_7.png')
    plt.axis('equal')

plot_ellipse(-6, 6, 1000)
