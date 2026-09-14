b1={'snack1','snack2','snack3'}
b2={'snack4','snack2','snack7'}
print('first basket has',b1)
print('second basket has ',b2)
a=b1.intersection(b2)
print('common snack in both is',a)
b1.add('banana')
print('basket 1 after adding banana ',b1)

import array as ar
a1=ar.array('i',[1,2,3,4,3,4])
print('original array is',a1)
z=a1.count(3)
print('number of occurence of 3 in array',z)
a1.reverse()
print('reverse of the array',a1)
a1.insert(0,1)
a1.append(7)
print('array after adding 7',a1)
