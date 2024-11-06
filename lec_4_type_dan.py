def changer(a, b):
    a = 2
    b[0] = 'Good'
 
x = 10
L = [1, 2]
 
changer(x, L)
 
print(x)
print(L)
 
L = [1, 2]
changer(x, L[:])
 
print(L)

# Coplex numbers
x = 3
y = 4

z = complex(x,y)
print(z)

w = complex(y, x)

print(z + w)

# Strings
s = 'hello'
print(s[0])