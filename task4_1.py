def mult_func(a):
    s = 0 
    for i in range(len(a)) :
        s += a[i]
    return s / len(a)

a = [1, 2, 3, 5, 10]
print(mult_func(a))
