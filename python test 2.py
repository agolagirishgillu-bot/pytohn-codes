import random
ops=['subtract','multiplication','division','add']
c=random.choice(ops)
print('random operation is',c)
try:
    a=float(input('enter a num:'))
    b=float(input('enter a num:'))
except ZeroDivisionError:
    print('pls enter num other than 0')
except ValueError:
    print('enter a valid num')

if c=='subttract':
    def subtract(a,b):
        d=(a-b)
        return(d)
    e=subtract(a,b)
    print(e)
elif c=='add':
    def add(a,b):
        f=(a+b)
        return f
    g=add(a,b)
    print(g)
elif c=='mutliplicatoin':
    def multiplication(a,b):
        h=(a*b)
        return h
    z=multiplication(a,b)
    print('ans is ',z)
elif c=='division':
    def division(a,b):
        j=(a/b)
        return j
    k=division(a,b)
    print(k)