m=int(input('enter your maths marks'))
eng=int(input('enter your eng marks'))
sci=int(input('enter your sci marks'))
avg=(m+eng+sci)/3
if avg in range(0,10):
    print('your grade r E2')
elif avg in range(10,50):
    print('your grade are B1')
elif avg in range (50,80):
    print('your grade are A2')
elif avg in range(80,101):
    print('your grade are a1')