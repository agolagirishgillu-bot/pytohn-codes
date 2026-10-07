class point:
    def __init__(self,x=0,y=1):
        self.x=x
        self.y=y

    def __str__ (self):
        return ('value of x is {} and value of y is {}'.format(self.x,self.y))

p1=point(5,10)
print(p1)