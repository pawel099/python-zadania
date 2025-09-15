import sqlite3
import sys

class engine:

 def __init__(self,baza):
        
        self.connection = sqlite3.connect(baza)
        self.cursor = self.connection.cursor()

        
 def createUser(self,users):
     
      self.cursor.execute(f"INSERT INTO student (name) VALUES ('{users}')")
      print("nowego dodano uzytkownika ")
      self.connection.commit()
 

 def update(self,old_name,_new_user) :
        input("nowa nazwa " + _new_user) 

         
        
        self.cursor.execute(f"UPDATE student SET name ='{_new_user}' WHERE name ='{old_name}'")
        self.connection.commit() # Zatwierdź zmiany
        print("pomyślnie zmodyfikowano użytkownika ")
         
 def removeUser(self,user:str):
      
       
      
      self.cursor.execute(f"DELETE FROM student WHERE name='{user}'")
      self.connection.commit()
      print("usunieto uztkownika ")
      
 def viewRekord(self) :
        
           wynik = self.cursor.execute("SELECT * FROM student ") 
           
           table = wynik.fetchall() 
           for dane in table:
                print(str(dane[0]) + " " +  dane[1])
           
               
polacz = engine('zadania\\aplikacje\\baza-uzytkowników\\baza-python.sqlite')
  
print("wybierz 0 by  zakonczyć ..")
print("wybierz 1 by wyswietlić wszystkich uzytkowników ..")
print("wybierz 2 by usunać użytkownika .. ")
print("wybierz 3 by edytować użytkownika .. ")
print("wybierz 4 aby dodać użytkownika .. ")


while True:

 match int(input('')):

  case 0:
   sys.exit(0) 

    
  case 1:
      polacz.viewRekord()

  case 2 :
      remove_user = input('podaj nazwę użytkownika..')
      polacz.removeUser(remove_user)      

  case 3:
      
      old_name = input('wpisz nazwę uzytkownika ')
      name = input ('wpisz nowa nazwę uzytkownika  .. ')
      polacz.update(old_name, name)

  case 4:
        name_user = (input('podaj nazwę uzytkownika..'))
        polacz.createUser(name_user)


    
