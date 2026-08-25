v=False
while not v:
    try:
        bill_amt,people,discount=input('enter the amts wiht comma in between').split(',')

        bill_amt=float(bill_amt)
        people=int(people)
        discount_per=float(discount)

        if bill_amt or people or discount_per==0:
            print('enter ')

        discount_a=(discount_per*people)/100
        final_amt=bill_amt-discount_a

        amt_per_person=final_amt/people
        v=True
    except SyntaxError:
        print('pls enter a valid amt')
    except ZeroDivisionError:
        print('pls enter a valid amt o')
    else:
      print('======SHOP SUMMARY======')
      print('people served',people)
      print('discount given',discount_a)
      print('final amt',final_amt)

    finally:
        print('bye')