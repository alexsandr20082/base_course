import numpy as np
g = 9.8
x0 = 0
y0 = 0
V0x = 10
V0y = 15
time = np.linspace(0,0.5,num=5) 
results  = ()
for t in time :
    x = x0 + V0y * t
    y = y0 + V0y * t - (g * t**2) / 2 (results.append(t,x,y0))
result_array = np.array(results)
print("Результаты (t,x,y): ")
print (result_array)