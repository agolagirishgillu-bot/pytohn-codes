class pet:
    name='Prayag'
    print('Welcome to the Pet Management by',name)

ob=pet()

class petclass:

    animal_type='dog'

    def __init__(self,name,age,fav_food):
        self.name=name
        self.age=age
        self.favorite_food=fav_food

pet1=petclass('tommy',10,'biscuites')
pet2=petclass('mike',12,'fish')

print('{} is a pet'.format(pet1.name))
print('{} is a pet'.format(pet2.name))

print('{} is a {} and its age is {} and its favrite food is {}'.format(pet1.name,pet1.animal_type,pet1.age,pet1.favorite_food))
print('{} is a {} and its age is {} and its favrite food is {}'.format(pet2.name,pet2.animal_type,pet2.age,pet2.favorite_food))