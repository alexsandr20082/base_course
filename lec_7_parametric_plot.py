import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(R=3) :
    alha = np.arange (-2 * np.pi, 2 * np.pi, 0.1)

    x = R * np.cos(alha)
    y = R * np.sin(alha)
    plt.plot(x, y, ls='--', lw=3)
    plt.axis('equal')
    plt.savefig('fig_1.png')
    
if __name__ == '__main__':
    circle_plotter()
