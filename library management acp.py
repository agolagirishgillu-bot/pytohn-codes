books=['hary poter','wonder','charlie']
books_quantity=[2,0,3]
library={books:count for books,count in zip(books,books_quantity)}
print(library)

available_books=[book for book in books if library[book] >0]
print(available_books)

book_to_read=input('enter the book you want:')
if book_to_read  not in available_books:
    print('that book is not in library')
    exit()
else:
    print('IT IS IN LIBRARY')
late_fees=[5,8,4,6,7]
extra_fees=int(input('enter the extra fees:'))
upd_library=list(map(lambda fee:fee+extra_fees,late_fees))
print(upd_library)

library[book_to_read]=library[book_to_read]-1
print(library)

print('========SUMMARY=========')
print('name of the books ',books)
print('book chosen to read',book_to_read)
print('fees paid',upd_library)
