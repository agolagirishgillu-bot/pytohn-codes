total_chores=4
original_num=total_chores
print(f'you have {original_num} chores to do ')

complete_count=0
chore_num=1

while chore_num<=total_chores:
      if chore_num==1:next_chore=print('to do english HW')
      elif chore_num==2:next_chore=print('to do maths HW')
      elif chore_num==3:next_chore=print('to do sst hw')
      else: next_chore= print('to do sci hw')

      a=input('you have finished your hw(yes/no)')

      if a=='yes':
       complete_count+=1
       chore_num+=1

       print('GREAT JOB!')

      else:
        print('do your hw now')

print('==============TODAYS HW SUMMARY===========')
print('total chores',total_chores)
print('completed chores',complete_count)
print('remaining chores',total_chores-complete_count)
