import math

a = 0
b = 4
l = 0.001
cont = 0

def f(x):
    return (x**2 - 8*x + 4)

c = b -a
tol = 0.0001
x0 = (a+b)/2
Ni = 100
while (c > l or math.fabs(f(x0)) > tol):
    if (f(a)*f(x0) < 0.0):
        b = x0
    elif (f(a)*f(x0) > 0.0):
        a = x0
    c = b - a
    x0 = (a + b) / 2
    cont += 1
    if (cont >= Ni):
        break
print(x0)




