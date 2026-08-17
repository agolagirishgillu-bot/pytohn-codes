def fact(x):
    '''this is a fact of the numbers'''

    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
print(fact.__doc__)
print('fact of 10 is',fact(10))
print('fact of 5 is',fact(5))
print('fact of 4 is',fact(4))
print('fact of 3 is',fact(3))