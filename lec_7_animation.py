import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation 
fig, ax = plt.subplots()
anim_object, = plt.plot([],[],'-',lw=2)
# [],[], два массива для передачи x и y
x,y = [],[]
parametr = np.linspace(0, 2*np.pi, 100) # Множество значений параметра	
ax.set_xlim(0,2*np.pi) 
ax.set_ylim(-1,1) 
def update(frame):
    x.append(frame)
    y.append(np.sin(frame))
    anim_object.set_data(x,y)
    return anim_object

	
ani = FuncAnimation(fig,update,frames=parametr,interval=50)
# Интервал это fps, то есть частота кадров в секунду 
ani.save('animation_1.gif', writer="pillow") # save при сохранении анимации, не savefig как график 