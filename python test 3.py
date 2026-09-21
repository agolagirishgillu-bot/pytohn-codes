students={'id1':{'name':'jack','score':'10'}
          ,'id2':{'name':'emma','score':'30'}
          ,'id3':{'name':'ally','score':'35'}
          ,'id4':{'name':'charlie','score':'40'}
          ,'id5':{'name':'john','score':'50'}}
print(students)

print(students.get('id1','not found'))

print(max(students))
print(min(students))

search=input('enter the u wnat to search')
if search not in students:
    print('not found in list')
else:
    print(students.get(search))