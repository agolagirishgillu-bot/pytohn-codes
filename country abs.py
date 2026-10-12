class india():
    def capital(self):
        print('india capital is new delhi.')

class usa():
    def capital(self):
        print('usa capital is wasinton d.c .')

obj1=india()
obj2=usa()

for i in(obj1,obj2):
    i.capital()
    