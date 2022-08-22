a = 6
b = 10
k = int(input())
ac = 0
e = 0.1
raiz = 0
x = b
ax = a
bx = b
prod = 0
while ac < k:
    print((a**2-8*a+4)*(x**2-8*x+4))

    prod = (a**2-8*a+4)*(x**2-8*x+4)
    if prod < 0:
        x = float((a + b) / 2)
        b = x
        print("LACO 1")
        if (b - a) <= e:
            raiz = x
            print(a-b)
            print("entro")
            break


    else:
        x = float((a + b) / 2)
        print("LACO 2")
        a = x
        if (b - a) <= e:
            raiz = x
            print(a-b)
            print("entro")
            break

    print(a, b, x)
    print(ac)
    ac += 1
print(raiz)






a = 6
b = 10
e = 0.001

def conta(a, b, e):
    prod = (a**2-8*a+4)*(b**2-8*b+4)
    print(a,b)
    x = float((a + b) / 2)
    bx = b
    ax = a
    if prod < 0:
        print("Laço 1")
        #print(a, b)
        print(prod)
        if (b - a) < e:
            return x

        b = x
        if prod > 0:
            b = bx
            a = x
            return conta(a, b, e)
        else:

            return conta(a, b, e)
    else:
        print("Laço 2")
        #print(a, b)
        print(prod)
        if (b - a ) < e:
            return x
        a = x
        if prod > 0:
            a = ax
            b = x
            return conta(a, b, e)
        else:

            return conta(a, b, e)


print(conta(a, b, e))
