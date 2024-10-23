import numpy as np
h = 100
g = 9.8
a = np.radians(45)
b = np.radians(35)
v = np.sqrt((g * h * np.tan(b)**2) / (2 * np.cos(a) * (1 - np.tan(b) * np.tan(a))))
print("Скорость v:",v,"м/с")

T = 200
k = 1,380649e-23
E = 300
N = ((2 / np.sqrt(np.pi)) * (h / (k * T)**(3/2)) * (-E / (k * T)) * (T/2))
print ("N:",N)