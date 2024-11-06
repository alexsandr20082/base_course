array = []
max_elements = 10
print("Введите до 10 чисел (нажмите Enter без ввода для завершения):")
for i in range(max_elements):
    user_input = input(f"Введите элемент {i + 1}: ")
    if user_input:  
        array.append(float(user_input))  
    else:
        break  
print("Введённый массив:")
print(array)


new_value = float(input("Введите новое значение для вставки: "))
position = int(input(f"Введите позицию (1-{len(array)+1}) для вставки нового значения: "))