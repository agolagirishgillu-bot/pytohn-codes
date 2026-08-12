secret=int(input('enter your secret no'))
yr_ans=int(input('enter your ans'))
guess=5
g=secret-yr_ans
guessing=True

while guessing:
    if yr_ans==secret:
        print('you guessed it!')
    else:
        print('wrong ans')
    if g in range(1 , 6):
            print(' hint:hot')
    else:
            print('hint :cold')
    break
      
guess-=1

print('you have chances left',guess)
if guess==0:
   print('ohh your all guess are over')

again=str(input('do u want to play agin:'))
if again=='no':
      print('bye! ')
else:
      
      yr_ans=int(input('enter your ans'))
      guess=5
      g=secret-yr_ans
      guessing=True

      while guessing:
          if yr_ans==secret:
            print('you guessed it!')
          else:
            print('wrong ans')
          if g in range(1 , 6):
            print(' hint:hot')
          else:
            print('hint :cold')
          break
      
guess-=1
print('you have chances left',guess-1)
if guess==0:
   print('ohh your all guess are over')

again=str(input('do u want to play agin:'))
if again=='no':
      print('bye! ')
else:
      
      yr_ans=int(input('enter your ans'))
      guess=5
      g=secret-yr_ans
      guessing=True

      while guessing:
          if yr_ans==secret:
            print('you guessed it!')
          else:
            print('wrong ans')
          if g in range(1 , 6):
            print(' hint:hot')
          else:
            print('hint :cold')
          break
      
guess-=1
print('you have chances left',guess-2)
if guess==0:
   print('ohh your all guess are over')

again=str(input('do u want to play agin:'))
if again=='no':
      print('bye! ')
else:
      
      yr_ans=int(input('enter your ans'))
      guess=5
      g=secret-yr_ans
      guessing=True

      while guessing:
          if yr_ans==secret:
            print('you guessed it!')
          else:
            print('wrong ans')
          if g in range(1 , 6):
            print(' hint:hot')
          else:
            print('hint :cold')
          break
      
guess-=1
print('you have chances left',guess-3)
if guess==0:
   print('ohh your all guess are over')

again=str(input('do u want to play agin:'))
if again=='no':
      print('bye! ')
else:
      
      yr_ans=int(input('enter your ans'))
      guess=5
      g=secret-yr_ans
      guessing=True

      while guessing:
          if yr_ans==secret:
            print('you guessed it!')
          else:
            print('wrong ans')
          if g in range(1 , 6):
            print(' hint:hot')
          else:
            print('hint :cold')
          break
      
guess-=1
print('you have chances left',guess-4)
if guess==0:
   print('ohh your all guess are over')
