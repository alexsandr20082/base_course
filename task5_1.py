import numpy as np
N = int(input("Введите длину массивов N: "))
array1 = np.random.randint(0, 101, size=N)
array2 = np.random.randint(0, 101, size=N)
array3 = np.random.randint(0, 101, size=N)

print("Первый массив:", array1)
print("Второй массив:", array2)
print("Третий массив:", array3)

max_element = max(np.max(array1), np.max(array2), np.max(array3))
print("Наибольший элемент среди всех трех массивов:", max_element)

total_sum = np.sum(array1) + np.sum(array2) + np.sum(array3)
print("Сумма всех элементов созданных массивов:", total_sum)