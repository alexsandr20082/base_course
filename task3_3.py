import numpy as np
g = 9.81
x0 = 0
y0 = 0 
V0x = 10
time_steps = np.linspace(0,0.5,num=100)
results = []
for t in time_steps:
    x = x0 + V0x * t
    y = y0 + V0x * t - (g * t**2) / 2
    results.append([t,x,y])
results_array = np.array(results)
print(results_array)
