class Account:
 
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin   
 
    def show_pin_status(self):
        print("Account Owner:", self.owner)
        print("PIN is safely stored inside the class.")
 
 
    def check_pin(self, entered_pin):
        if entered_pin == self.__pin:
            print("Access granted.")
        else:
            print("Access denied.")
 
    def __str__(self):
        return "Account holder: " + self.owner
 
 
my_account = Account("Riya", "1234")
 
print(my_account)
 
my_account.show_pin_status()

my_account.__pin = "9999"
print("Tried changing PIN directly from outside.")
 
my_account.check_pin("9999")
my_account.check_pin("1234")
 

my_account.check_pin("9999")