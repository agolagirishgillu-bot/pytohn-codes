print('HOLIDAY PLANNER')

place_selection=int(input('enter your place'))
print('step 1 choose your place')
print('1 for goa')
print('2 for kashmir')

if place_selection ==1:
   print('you have selected goa')
   print('famous for beaches')

else:
   print('you have selected kashmir')
   print('famous for natural sighting')

mode_of_transport=int(input('enter your mode of transport'))
print('step 2 choose your mode of transport')
print('1 for plane')
print('2 for train')
    
if mode_of_transport ==1:
   print('you have chosen plane')
   print('it is comfortable but cotly')
   print('you reaches your place quickly')

else:
    print('you have chosen train')
    print('it is not comfortable but it is cheaper')
    print('you will reach your place late')

if mode_of_transport and place_selection==3:
   print('invalid option')
   print('please select a correct option')
else:
   print('YOUR HOLIDAY PLANNER IS READY')
   print('ENJOY YOUR HLOIDAYS')