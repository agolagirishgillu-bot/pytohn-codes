import math
import random

print('welcome to the game!')
l_n=random.randint(1,10)
print('your lucky no is',l_n)
p=['guessing number']
f_a=random.choice(p)
print('your fun activity is',f_a)

while True:
    print('computer will be chosing a random number 0 to 5')
    s_n=random.randint(0,5)
    g=int(input('enter your ans:'))

    if s_n==g:
        print('u win')
        break
    else:
        print('u lose')

# math module
print('wel come to the math ')
d=float(input('enter a number:'))
a=math.ceil(d)
print(a)
b=math.floor(d)
print(b)      
z=100
t=1000
c=math.copysign(z,t)
print(c)
e=math.gcd(z,t)
print(e)


print('summary')
print('lucky no',l_n)
print('fun activity',f_a)