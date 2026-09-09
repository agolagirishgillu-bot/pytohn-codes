t_d={'name':2,'class':2,'sub':2}
print('the original dict',(t_d))
k=2
res=0
for keys in t_d:
    if t_d[keys]==k:
        res+=1

print('the frequency is',str(res))