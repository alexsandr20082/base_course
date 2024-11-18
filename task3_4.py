import numpy as np
N = int(input("Введите число N (число строк): "))
M = int(input("Введите число M (число столбцов): "))

trigonometry_array = np.zeros((N, M))

for i in range(N):
    for j in range(M):
        value = np.sin(N * i + M * j + 1)
        trigonometry_array[i, j] = value if value >= 0 else 0

print("Конечный массив:")
print(trigonometry_array)