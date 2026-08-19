def cal_change(paid, price):
    change=paid-price
    print(f'hi here is your {change} change')
    return change



s=25
print('welcome to vending machine')
print('the price of yuor snack is ',s)
print('enter a coin')

total_inserted=0
coin_inserted=0

while True:

    coin=int(input('enter the coin'))


    if coin!=1 and coin!=5 and coin!=10 and coin!=25:
        print('enter a valid coin')
        continue

    total_inserted+=coin
    coin_inserted+=1
    print(f'inserted {coin} total so far {total_inserted}')

    if total_inserted>=s:
        print('u paid enough')
        break

change_due=cal_change(total_inserted,s)

print('dispensing yr snack......')

print('vending machine summary')
print('snack price',s)
print('total revenue',total_inserted)
print('coins inserted',coin_inserted)
print('total change given',change_due)