def cube(n):
    return n*n*n

def by_three(n):
    if n % 3==0:
        return cube(n)
    else:
        print('false')

print(by_three(9))
print('hi')
print(by_three(4))
print('and')