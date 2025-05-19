def add_exponse(month):
    print()
    exponse_amount = int(input("podaj kwotę [zl]: "))
    exponse_type =   int(input("podaj typ wydatku ('jedzenie,rozrywka,dom , inny): "))

    expanse = ( )

while True:
  print()
  month = int (input("Wybierz miesiąc [1-12]:"))

  if month==0:
   break
  
while True: 
  
  print()

  print("0. Powrót do wyboru miesiąca")
  print("1 wyświetl wszystkie wydatki")
  print("2 dadaj wydatek")

  choice = int(input("wybierz opcję: "))

  if choice == 0 :
    
    break
  
  if choice == 1:

   print("wszystkie wydatki")

  if choice ==2:
   add_exponse()






     






