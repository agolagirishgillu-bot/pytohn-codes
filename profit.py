actual_price=float(input('enter actual_price'))
sale_price=float(input('enter sale_price'))
if actual_price<sale_price:
    amt=sale_price-actual_price
    print('total profit',amt)
else:
    print('no profit')
