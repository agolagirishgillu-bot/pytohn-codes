class iostring():
    def __init__(self):
         self.str1=''

    def get_ans (self):
          self.str1=input('enter a word')
    def print_ans(self):
          print(self.str1.upper())
         
hi=iostring()

hi.get_ans()
hi.print_ans()