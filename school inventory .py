items=['glue','eraser','pen','sharpener']
print(items)
items_q=[7,0,6,4]
print(items_q)
inv= {items:count for items,count in zip(items,items_q)}
print(inv)

items_chosen=input('enter the item u want')
if items_chosen in inv:
    print('in stock')
    exit()
else:
    print('out fo stock')


print('=====SUMMARY=====')