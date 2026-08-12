def greet_customer():
    print('welcome')

greet_customer()

price=float(input('enter the amount of cups:'))
cups=int(input('enter the no of cups sold:'))

def total_cost(price,cups):
    total_price=cups*price
    return total_price
a=total_cost(price,cups)
print(a)

def amount_paid(a):
    amt=float(input('enter your amount:'))
    change=a-amt
    return change


b=amount_paid(a)
print(b)