import numpy as np
N = 5
M = 15
trigonometry_array = np.zeros((N,M))
for i in range(N):
    for j in range(M):
        reply = np.sin(i * M * j)
        trigonometry_array[i][j] = max(reply,0)
print("Исходный массив: ")
print(trigonometry_array)
pop1,pop2 = 0,1
trigonometry_array[:, [pop1,pop2]] = trigonometry_array[:, [pop1,pop2]]
print("Массив после замены столбцов: ")
print(trigonometry_array)
 
