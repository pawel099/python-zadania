 
import sqlite3
import sys

class student:
    
    def __init__(self,baza):
        self.connection = sqlite3.connect(baza)
        self.cursor = self.connection.cursor()
        

    def createUser(self):
     
     users = [
          
     ]

     sql_insert = "INSERT INTO student (id, name) VALUES (?, ?)"
     self.cursor.executemany(sql_insert,users)
     self.connection.commit()

    def removeUser(self,user):
     #self.cursor.execute(f"DELETE FROM student WHERE id={user}") 
     print(f"DELETE * FROM student WHERE id ={user}")
       

      

    def viewRekord(self):
        
        wynik = self.cursor.execute("SELECT * FROM student")   
        table = wynik.fetchall()
        return table
    

polacz = student('zadania\\aplikacje\\baza-uzytkowników\\baza-python.sqlite')
 
#polacz.createUser()
input 
polacz.removeUser(10)
print("wybierz 1 by wyswietlić rekordy ..")
print("wybierz 2 by usunać rekord .. ")
dane = int(input())


match dane:

 case 2:
      
      identyfikator = int(input(" podaj id uzytkownika "))
      polacz.removeUser(identyfikator) 
      print("usunieto uztkownika")
      sys.exit(0)     

 case 1:
      
  dane = polacz.viewRekord()

for users in dane:
    print(users)

   
  
 
 


  
  



    

