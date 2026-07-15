a=int(input('enter the speed'))
b=int(input('enter the speed'))
c=int(input('enter the speed'))

avg=(a+b+c)/3
print(avg)

if avg >a and avg >b and avg >c:
    print('they all r slower than avg speed ')
elif avg >a and avg >b:
    print('a and b r slower')
elif avg >a and avg >c:
    print('a and c r slower')
elif avg >a:
    print('a is slower')
elif avg >b:
    print('b is is slower')
elif avg >c:
    print('c is slower')