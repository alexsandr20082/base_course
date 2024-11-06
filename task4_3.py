def mult_func(a):
    energy1 = m * g * h
    energy2 = 0.5 * m * v**2
    energy = energy1 + energy2
    return energy

v = int(input("Введите скорость тела : "))
h = int(input("Введите высоту  : "))
m = int(input("Введите массу тела : "))

g = 9.8
energy_total = mult_func(g)

print("Полная механическая энергия тела: ", energy_total)
