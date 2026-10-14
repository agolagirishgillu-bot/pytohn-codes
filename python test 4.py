book={'book1':1,'book2':2,'book3':4}
print(book)
class books:
    def __init__(self,title,author):
        self.title=title
        self.author=author


    def detail(self,c):
        self.c=c=input('enter the book which u want to borow:')
    
        print(book.get(c))

    def borrow(self):
            print('borrowed successfully!')

            print(book)==book[self.c]-1

    def return_(self):
        e=input('do u want to return the book:')
        if e=='yes':
            print('verify it.')

            f=input('enter the books name')
            if f==self.c:
                print('ok returned!')

            print(book)==book[self.c]+1

            


b=books('HELLO','HI')
b.title
b.author
b.detail(10)
b.borrow()
b.return_()
    