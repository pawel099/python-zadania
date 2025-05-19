
import sqlite3
import sys

baza = sqlite3.connect("")

def login():

 login = input("podaj swój login: ")
 password = input("podaj swoje hasło: ")

 dane = baza.execute("SELECT * FROM users")
 tabela = dane.fetchall()

 
 for table in tabela:
  if login == table[0] and password==table[1]:
     return table
 else:
     error = "wystapił bład"

 print(error)   
user = login()

def view():
 
 try:
 
  wynik = "SELECT name from user WHERE id = " + str(user[0])
  user = baza.execute(wynik)
  users = user.fetchall()

  return users

 except:
   
   return False
   
r = view()
 
print(r)






 
 



                
                 
             
      
 





 

            


  
 
  
  
     


    





 


       


    
    
          
 


    



  
      

  
 
 

 


 
