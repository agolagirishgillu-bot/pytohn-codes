b1={'mango','banana','kiwi'}
b2={'mango','banana','apple'}
print(b1)
print(b2)
d=b1.intersection(b2)
print(d)
import array as arr
a=arr.array('i',[1,2,3,4,5])
print(a)

a.insert(0,1)
a.append(6)
print(a)
a.reverse()
print(a)
z=arr.array[1,2,33,44,44,44]
print(z)
t=z.count(44)
print(t)
print('=======SUMMARY=====')
print('fruits in basket 1',b1)
print('fruit in basket 2',b2)
print('common fruit in both baskets',d)
print('array 1',a)
print('array 2',z)
print('count of 44 in array 2',t)