rows = 4
cols = 3
array1 = [[0] * cols for _ in range(rows)]
array2 = [[0] * cols for _ in range(rows)]
array3 = [[0] * cols for _ in range(rows)]
print("Введите элементы первого массива (4x3):")
for i in range(rows):
    for j in range(cols):
        array1[i][j] = int(input(f"array1[{i}][{j}]: "))
print("Введите элементы второго массива (4x3):")
for i in range(rows):
    for j in range(cols):
        array2[i][j] = int(input(f"array2[{i}][{j}]: "))
for i in range(rows):
    for j in range(cols):
        array3[i][j] = max(array1[i][j], array2[i][j])
print("Третий массив (большие элементы):")
for row in array3:
    print(row)