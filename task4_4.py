import numpy as np
def values(a,b,N):
    x_values = np.linspace(a,b,N)
    y_values = x_values**2
    return y_values
a = int(input("Введите первый промежуток "))
b = int(input("Введите второй промежуток "))
N = int(input("Введите чсило точек "))
print(values(a,b,N))