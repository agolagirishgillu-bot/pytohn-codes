class Class:

    __private_variable=27

    def __privmeth(self):
        print('i am in a private class.')

    def hello(self):
        print('class private varialbe is:',Class.__private_variable)

h1=Class()
h1.hello()

