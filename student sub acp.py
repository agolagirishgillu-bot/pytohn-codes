st_d={'id1': {'name':'sara','class':'5','sub':'eng'},
      'id2':{'name':'sary','class':'4','sub':'math'},
      'id3':{'name':'sara','class':'5','sub':'eng'}}
print('the original dict is',st_d)

print('details of id1.')
print(st_d.get('id1','not found'))

print(st_d.get('id5','not foundd'))

st_d['id4']={'name':'jack','class':'6','sub':'coding'}
print('after adding update')
print(st_d)

st_d['id2']['sub']='eng, math, coding'

print('after updating id2')
print(st_d)
print(len(st_d))

s_r=[]
c_d={}

for student_id,detail in st_d.items():
    u_k=(detail['name'],detail['class'],detail['sub'])

    if u_k not in s_r:
        s_r.append(u_k)
        c_d[student_id]=detail

st_d=c_d

print('after deleting double ids')
print(st_d)

r_s=st_d.pop('id2','not found')
print(r_s)