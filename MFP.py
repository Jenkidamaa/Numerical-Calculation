import math

a = 1
b = 5
l = 0.001
cont = 0
xo = 0

def f(x):
    return (x**3-9*x+3)

c = b -a
fa = f(a)
fb = f(b)

while abs(fa)>l or abs(fb)>l or (b-a)>l:
  c = b -a
  fa = f(a)
  fb = f(b)
  xo = a
  x1 = (a*fb-b*fb)/(fb-fa)
  if f(x1)<l or (b-a)<l:
    x1 = a + b
    break
  if fa*f(x1)>0:
    a = x1 
    fa = f(x1)
    if f(x1)*f(xo)>0:
      fb = fb/2
  b = x1
  fb = f(x1)
  if f(x1)*f(xo)>0:
    fa = fa/2
  f
  cont += 1

print(cont)
