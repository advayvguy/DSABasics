class Bankaccount:
    
    def __init__(self):
        self.name = None
        self.age = None
        self.balance = 0
    
    def filldetails(self):
        self.name = input("enter name: ")
        self.age = input("enter age: ")
        self.balance = int(input("add balance: "))

    def add(self,plus):
        self.balance = self.balance + plus

    def sub(self,minus):
        if (minus > self.balance):
            print("not enough balance")
        else:
            self.balance = self.balance - minus
    
    def __str__(self):
        return f"name: {self.name}, age: {self.age}, balance: {self.balance}"
