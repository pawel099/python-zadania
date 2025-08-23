
expenses = []

def show_expenses(month):
   
   for expanse_amount ,expanse_type, expanse_month in expenses:
      if expanse_amount == month:
         print(f'{expanse_amount} - {expanse_type}')
      

def add_expense(month):
   print()

   expanse_amount = int(input(" podaj kwotę [zl] "))
   expanse_type = input("podaj kategorię wydatku [jedzenie, rozrywka, dom, inny] ")

   expose = (expanse_amount,expanse_type,month)
   expenses.append(expose)

   print("dodano wydatek")

def show_stats(month):
   total_amount_this_month = sum(expanse_amount for expanse_amount in expenses if expanse_amount==month)
   
   print()
   print("Statystyki")
   print("wszystkie wydatki w tym miesiącu" , total_amount_this_month)


while True:

    print()
    month = int(input(" wybierz miesiąc [1-12]: "))

    if month == 0 :
       break 

    while True:
      
      print(" 0. Powrót do wyboru miesiąca ")
      print(" 1. wyswietl wszystkie wydatki ")
      print(" 2. Dodaj wydatek ")
      print(" 3. Statystyki")



      choice = int(input("wybierz opcję: "))

      if choice == 0:
         break
      
      if choice ==1:
         show_expenses(month)
         
      if choice == 2:
         add_expense(month)
             
      if choice == 3:
         show_stats(month)  

         












 

