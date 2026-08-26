import random
computer_choice=random.randint(1,10)
print('comp. will select any number 1 to 10')
ans=int(input('enter tha num'))
if ans==computer_choice:
    print('u win')
else:
    print('not right')