from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
theta = np.linspace(0,1*np.pi,100)

def f (t):
    x = t - np.sin(t)
    y = 1 - np.cos(t)
    return x,y
fig,ax = plt.subplots(figsize=(8,6))
ax.set_xlim(-15,15)
ax.set_ylim(-15,15)
line, = ax.plot([],[])

def update(frame):
    t = frame/10
    x_c,y_c = f(np.linspace(0,t,100))
    line.set_data(x_c,y_c)
    return line,
ani = FuncAnimation(fig, update, frames=np.arange(0,200,1), interval=50)
ani.save('animation_4.gif', writer="pillow") 


