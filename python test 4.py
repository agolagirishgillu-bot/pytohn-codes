book={'book1':1,'book2':2,'book3':4}
print(book)
class books:
    def __init__(self,title,author):
        self.title=title
        self.author=author


    def detail(self,c):
        self.c=c=input('enter the book which u want to borow:')

        if c=='book1':
                print('books name is ',self.title)
                print('books author is ',self.author)
    
        print(book.get(c))

    def borrow(self):
            print('borrowed successfully!')

            book[self.c]=book[self.c]-1
            print(book)
           
    def return_(self):
        e=input('do u want to return the book:')
        if e=='yes':
            print('verify it.')

            f=input('enter the books name')
            if f==self.c:
                print('ok returned!')

                book[self.c]=book[self.c]+1
                print(book)

            else:
                 print('book not verified.')

        else:
             print('ok u do not want to return the book.')   


b=books('HELLO','HI')
b.detail(10)
b.borrow()
b.return_()