def mult_func(a,b,n):
    a = 0
    b = 10
    n = 5
    def f(x):
        return x **2
    y = []
    step = (b - a)/(n-1)

    for i in range(n):
        x = a + i * step
        y.append(f(x))
    return y
result = mult_func(a ,b ,n)
print(result)


