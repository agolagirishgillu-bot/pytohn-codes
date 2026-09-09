h=('writing',True,3.14)
print(h)
print(len(h))
print(h[:2])
t=(1,2,3,4)
print(t)
t1=t+h
print(t1)
t2=(20,41,41,45,20)
print(t2.count(20))
weekly_habits=(1,0,1,0,0,1)
not_done=0
done=0
if weekly_habits==0:
        not_done+=1
else:
        done+=1

if not_done<=1:
    print('complete your work.')
else:
    print('good job.')