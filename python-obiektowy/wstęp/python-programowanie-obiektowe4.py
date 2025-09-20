 #enkapsulacja

class Account:
    def __init__(self):
        self.amount = 0

    def deposit(self,amount:float):
            self.amount += amount
             

    def withdraw(self,amount:float):

        if self.amount<amount:
         raise ValueError("nie masz wystarczajacych srodków na koncie")
        
        self.amount-= amount

        return {

           'amount_left' : self.amount,
           'amount_withdraw' : amount,
        }
try:
   
   my_account = Account()
   my_account.deposit(1000)
    
   result = my_account.withdraw(60)
   print(result)

except ValueError as message:

 print(message)

 

