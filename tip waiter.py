def t_c(bill_amt,tip):
    total=bill_amt*(1+00.1*tip)
    total=round(total,2)
    print(f'pay{total}')

t_c(150,10)