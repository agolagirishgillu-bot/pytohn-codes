from abc import ABC ,abstractmethod

class Absclass(ABC):
    def class1(self):
        print('the value of x is ')

    @abstractmethod
    def task(self):
        print('we are in a absrtact class')

class new_class(Absclass):
    def task(self,x):
        print('we are in a new class')
        print('the value of x is',x)
        super().task()
new=new_class()
new.task(100)