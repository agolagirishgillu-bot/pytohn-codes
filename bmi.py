h=float(input('enter your height'))
w=float(input('enter your weight'))
bmi=w/(h/100)**2
if bmi ==18:
    print('u r underweight')
elif bmi <= 20:
    print('u r healthy')
elif bmi <= 30:
    print('u r obese')
else:
    print('u r severly obese')
