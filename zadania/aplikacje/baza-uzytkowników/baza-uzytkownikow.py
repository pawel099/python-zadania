<<<<<<< HEAD
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

   
  
 
 


  
  



    


=======

import sqlite3
import sys

class baza:
  
  def __init__(self,polacz:str):
 

    self.connection = sqlite3.connect(polacz)
    self.cursor = self.connection.cursor()
    
    
    self.create_table()


  def create_table(self):
     
     self.cursor.execute('''CREATE TABLE IF NOT EXISTS student (
       id INTEGER PRIMARY KEY ,
       name TEXT NOT NULL
       )
     ''')

  def insert_user(self):

    self.cursor.execute('''
    INSERT INTO student (id, name)
    VALUES(1,pawel)                   

   '''


    )
    
  def commit(self):

    self.connection.commit()


  def pobierzRekord(self,user:str):

     self.cursor.execute('SELECT id ,name FROM student')
     uzytkownik = self.cursor.fetchall()

     for wynik in uzytkownik:
      return wynik 

  def close(self):

    self.close()

    

polaczenie = baza('baza.sqlite')
uzytkownik = int(input('wpisz id użytkownika: '))

wynik = polaczenie.pobierzRekord(uzytkownik)

print(wynik)


  





   
>>>>>>> ad0ec887eb8e5c6c29a01d248f5391e2e6239721
 
 
 
 












