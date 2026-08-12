def greet_customer():
    print('welcome to the store')

greet_customer()
customer=0

item_name=str(input('enter the product name:'))
p=float(input('enter the  price:'))
q=int(input('enter the quantity:'))

def total_cost(p,q):
    t_p=p*q
    return t_p
a=total_cost(p,q)
print(a)
amt_paid=float(input('enter the amt you paid:'))
def change_due(amt_paid,t_p):
    change=amt_paid-t_p
    return change
b=change_due(amt_paid,a)
if a>amt_paid:
    print('you have paid less')
else:
    print(f'here is your change that is {b}')
def thank_you_msg():
    print('thank you . please visit agian')

thank_you_msg()
customer+=1

print('=====store summary===========')
print('total rveneu',a)
print('no of customer served',customer)
print('item bought',item_name)