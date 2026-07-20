print('===============================')
print('WELCOME TO THE CUSTOM BIKE RIDE')
print('===============================')
print()

print('1 = bike   2 = car')
print()

c=int(input('enter your choice'))
if c==1:
    print('pick your bike type')
    print('1 = scooty')
    print('2 for mt. bike')


    bike_type=int(input('enter your bike_type'))
    if bike_type ==1:
        print('you picked scooty')
        print('speed is 40 km/h')
        print('best for city')
    else: 
        print('you picked mt. bike')
        print('speed is 50 km/h')
        print('best for off-road')
         

elif c==2:
    print('step 2 pick your car type')
    print('1 for sedan ')
    print('2 for SUV')
    car_type=int(input('enter your car_type'))

    if car_type ==1:
       print('you picked sedan')
       print('speed is 70 km/h')
       print('best for family trip')

    else:
        print('you picked SUV')
        print('speed is 70 km/h')
        print('best for OFF-road')

else:
    print('invalid choice')
    print('please enter 1 for bike and 2 for car')

print('========================================')
print('YOUR CUSTOM RIDE IS READY')
print('ENJOY YOUR JOURNEY')
print('========================================')
