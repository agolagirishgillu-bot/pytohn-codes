import random
while True:
   user_c=str(input('rock, paper, scissor'))
   p_a=['rock','paper','scissor']
   comp_c=random.choice(p_a)
   print(f'you chose {user_c} and comp choose {comp_c}  ')

   if user_c==comp_c:
      print('tie')
   elif user_c=='rock' and comp_c=='paper':
      print('u lose')
   elif user_c=='rock' and comp_c=='scissor':
      print('u win')
   else:
      print('in valid choice') 