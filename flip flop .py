def palind(r):
    e=len(r)-1
    s=0
    while True:
       if (r[e])!=(r[s]):
          return False
       else:
          return True

r=(1,2,3,3,2,1)
if palind(r)==False:
   print('not flip flop')
else:
    print('flip flop')