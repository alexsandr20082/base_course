import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

alpha = 0.1  
num_frames = 100 
phi = np.linspace(0, 2 * np.pi, 100)  

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
circle_line, = ax.plot([], []) 

def update(frame):
    r = alpha * frame  
    x = r * np.cos(phi)  
    y = r * np.sin(phi)  
    circle_line.set_data(x, y) 
    return circle_line,

ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)
ani.save('animation_5.gif', writer="pillow")