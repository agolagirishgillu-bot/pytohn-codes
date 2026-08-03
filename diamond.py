r=int(input('enter thr no of rows'))
if r%2==0:
    halfdiamond=int(r/2)
else:
    halfdiamond=int(r/2)+1
space=halfdiamond-1
for i in range(1,halfdiamond+1):
    for f in range(1,space-1):
        print(end='')
        space-=1
    n=1
for f in range(2*i,+1):
    space+=1
    n+=1
    
