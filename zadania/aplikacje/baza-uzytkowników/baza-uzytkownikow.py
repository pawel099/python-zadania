
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


  





   
 
 
 
 












