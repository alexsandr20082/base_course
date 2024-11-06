import numpy as np
def mult_func(a): 
    s = 1
    for i in range(len(a)) :
        s *= a[i]
    return s 
a = [1, 2, 3, 5, 10]
print(mult_func(a))



