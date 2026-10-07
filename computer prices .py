class comp:
    def __init__(self):
        self.__price=900

    def maxprices(self):
        print('computer max prices is:',self.__price)

    def newprice(self):
        self.__newprice = self.__price + 100
        print('new prices is:',self.__newprice)

h1=comp()
h1.maxprices()
h1.newprice()
h1.__newprice=2000
h1.newprice()