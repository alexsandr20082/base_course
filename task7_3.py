from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
theta = np.linspace(0,1*np.pi,100)

def f (t):
    x = sin(t) * (e**(t))
    y = 1 - np.cos(t)
    return x,y