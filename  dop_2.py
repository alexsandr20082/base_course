a = int(input("Введите длину первой стороны: "))
b = int(input("Введите длину второе стороны: "))
z = int(input("Введите длину третьей стороны: "))
if a + b > z and a + z > b and b + z > a:
    print ("Такой треугольник существует")
    if a == b == z:
        print("Треугольник равностронний")
    elif a == b or b == z or a == z:
        print("Треугольник равнобедренный")
    else:
        print ("Треугольник равностронний")