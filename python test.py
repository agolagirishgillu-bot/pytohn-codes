secret=int(input('enter your secret no'))
yr_ans=int(input('enter your ans'))
guess=5
g=secret-yr_ans
guessing=True
while guessing:
    if yr_ans==secret:
        print('you guessed it!')
    elif yr_ans!=secret:
        print('wrong ans')
        guess-=1
        if g in range(1 , 6):
           print('hot')
           
    
    break
for guess in range(1, 6):
    print('yr remaning chances',guess-1)
