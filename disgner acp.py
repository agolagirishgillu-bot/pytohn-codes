# for right angle triangle
r=int(input('enter the number of rows:'))

for i in range(r):
    for f in range(i+1):
        print('*',end='')
    print()
# for floyd triangle
rs=int(input('enter the no of rows:'))
n=1
for i in range(1, rs+1):
    for f in range(1,i+1):
        print(n ,end='')
        n+=1
    print()

n=1
for i in range(1,11,2):
    print('  '*(5-n),'* '*i)
    n+=1