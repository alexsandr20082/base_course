import numpy as np
N = 5
M = 15
trigonometry_array = np.zeros((N,M))
for i in range(N):
    for j in range(M):
        reply = np.sin(i * M * j)
        trigonometry_array[i][j] = max(reply,0)
print(trigonometry_array)
