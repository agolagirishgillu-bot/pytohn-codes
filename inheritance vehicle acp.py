class vehicle:
    def __init__(self,model,company):
        self.model=model
        self.company=company

        print('car model is',self.model)
        print('car brand is ',self.company)

class car(vehicle):
    def __init__(self, model, company,seat,speed):
        self.speed=speed
        self.seat=seat
        super().__init__(model,company)

    def details(self):
        print('car seat capacity is',self.seat)
        print('car top speed is ',self.speed)

    def more_detail(self,fuel):
        self.fuel=fuel
        print('cars fuel is',self.fuel)
        
h1=car('x','y',7,100)

h1.more_detail(fuel='petrol')

h1.details()

print('cars model is',h1.model)
print('cars company is ',h1.company)
