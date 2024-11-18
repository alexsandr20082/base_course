import numpy as np
N = int(input("Введите число N (число строк): "))
M = int(input("Введите число M (число столбцов): "))

trigonometry_array = np.zeros((N, M))
print("Исходный массив перед заменой столбцов:")
print(trigonometry_array)

col1 = int(input("Введите индекс первого столбца для замены (от 0 до {}): ".format(M - 1)))
col2 = int(input("Введите индекс второго столбца для замены (от 0 до {}): ".format(M - 1)))

if 0 <= col1 < M and 0 <= col2 < M:
    trigonometry_array[:, [col1, col2]] = trigonometry_array[:, [col2, col1]]
else:
    print("Некорректные индексы столбцов.")

print("Массив после замены столбцов:")
print(trigonometry_array)