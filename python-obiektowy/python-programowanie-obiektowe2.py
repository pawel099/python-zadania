class uzytkownik:

    def __init__(self,login,password):

        self.login = login
        self.password = password


    def user(self):
         
        users = {'pawel':'sekret1','anna':'sekret2'}
        
        for user in users.items():
            if user[0] == self.login and user[1] == self.password:
                 return True
            
        else:
            return False
                
podaj_login = input("podaj login: ")
podaj_haslo = input("podaj hasło: ")
             
e = uzytkownik(podaj_login,podaj_haslo)
print(e.user())



 



     


 
