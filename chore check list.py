total_chore=4
original_num=total_chore

print(f'you have {original_num}chores to finish today')

complete_count=0
chore_num=1

while chore_num <=total_chore:

      if chore_num==1:next_chore=print('make your bed')
      elif chore_num==2:next_chore=print('feed the pet')
      elif chore_num==3:next_chore=print('throw the trash')
      else: next_chore=print('wash the dishes')

      a=input(f'you have {next_chore} finished your chore(yes/no)')

      if a=='yes':
           complete_count+=1
           chore_num+=1
           print('great job')
        

      else:
           print('finish your chores then check again')

print('=================CHORES SUMMARY============')
print('chores assigned today',total_chore)
print('chores completed',complete_count)
print('cchores left to do',total_chore-complete_count)