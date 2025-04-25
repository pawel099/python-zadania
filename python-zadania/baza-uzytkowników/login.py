
import sqlite3
import sys

baza = sqlite3.connect("python-zadania\\baza-uzytkowników\\sqlite\\baza.sqlite")

def login():

 login = input("podaj swój login: ")
 password = input("podaj swoje hasło: ")

 dane = baza.execute("SELECT * FROM users")
 tabela = dane.fetchall()

 
 for table in tabela:
  if login == table[1] and password==table[4]:
     return table
 else:
     error = "wystapił bład"

 print(error)   
user = login()

def view():
 
 try:
 
  wynik = "SELECT name from products WHERE id = " + str(user[0])
  product = baza.execute(wynik)
  products = product.fetchall()

  return products

 except:
   
   return False
   
r = view()
 
print(r)






 
 



                
                 
             
      
 





 

            


  
 
  
  
     


    





 


       


    
    
          
 


    



  
      

  
 
 

 


 
