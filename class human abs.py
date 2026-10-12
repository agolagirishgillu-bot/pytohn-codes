from abc import ABC ,abstractmethod

class animal(ABC):
    def move(self):
        pass


class human(animal):
    def move(self):
        print('human can walk.')


class snake(animal):
    def move(self):
        print('snake can crawl.')


class bird(animal):
    def move(self):
        print('bird can fly.')


ani=bird()
ani.move()

an1=human()
an1.move()

an2=snake()
an2.move()