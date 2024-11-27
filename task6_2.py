import matplotlib.pyplot as plt
import numpy as np
def hyperbola_plotter(x1,x2,N):
    x = np.linspace(x1,x2,N)
    y1 = 1/x
    plt.plot(x,y1,color='black')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('hyperbola plotter')
    plt.legend()
    plt.savefig('fig_6.png')
 
 
if __name__ == '__main__':
    hyperbola_plotter(-10,10,100)

