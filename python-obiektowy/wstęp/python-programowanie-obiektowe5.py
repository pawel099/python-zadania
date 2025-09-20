 #metody specjalne

class Account:

    def __init__(self,amount:float):
        self.amount = amount

    def __str__(self):
        return f"saldo konta {self.amount}"
    
    def __repr__(self):
        return f"saldo konta {self.amount}"
    
    def __eq__(self,other):
        return self.amount == other.amount
    
    def __lt__(self,other):
        return self.amount == other.amount
    
    def __add__(self,other):
        return self.amount + other.amount
    
accounts = [

Account(1000),
Account(1200),
Account(2500),



] 

accounts.sort(reverse=True) 
print(accounts[0] + accounts[2])
print(accounts)

 
     
