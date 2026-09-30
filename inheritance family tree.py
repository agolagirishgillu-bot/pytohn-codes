class parent:
    def __init__(self,eye_color,height):
        self.eye_color=eye_color
        self.height=height
    def print1(self):
        print('this is parent class')
        print('eye color is',self.eye_color)
        print('height is in cm',self.height)


class kid(parent):
    def __init__(self,eye_color,height,age,name):
        self.age=age
        self.name=name
        super().__init__(eye_color,height)

        print('this is kid class')

    def print2(self):
        print('this is kid class')
        super().print1()
        print('name of the kid is',h1.name)
        print('age of the kid is',h1.age) 

    def function(self,hooby):
        self.hooby=hooby

        print('kid loves',hooby)

h1=kid('blue',120,10,'maya')

h1.function('painting')

h1.print2()
