def cal_c(price,paid):
    change=price-paid
    return change

ticket_price=50
print('welcome to the parking')
print('ticket price is 50')
print('pls enter a coin ')

total_in=0
coin_in=0

while True:
    coin=int(input('enter the coin'))

    if  coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print('pls enter a valid coin')
        continue
    total_in+=coin
    coin_in+=1

    print(f'inserted {coin}. total so far {total_in} ') 

    if total_in>=ticket_price:
        print('paid enough')
    
        break

change_due=cal_c(total_in,ticket_price)

print('u may go in ')

if change_due==0:
    pass
else:
    print(f'here is your change {change_due}')

print('summary ')
print('ticket price',ticket_price)
print('coin inserted',coin_in)
print('total revenue',total_in)
print('change given',change_due)