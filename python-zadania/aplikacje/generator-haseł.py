import sys
import random
import string

password = []
charakter_left =-1

def update_charakter_left(number_of_charakter):

    global charakter_left

    if number_of_charakter<0 or number_of_charakter>charakter_left:
       print("liczba znaków z poza przedziału 0 " ,charakter_left)
       sys.exit(0)
    
    else:
     charakter_left -= number_of_charakter
     print("pozostało znaków",charakter_left)


password_length = int(input("jak długie ma być hasło ? "))

if password_length<10:
    print("hasło jest za krótkie , musi mieć min 5 znaków")
    sys.exit(0)
else:
    charakter_left = password_length


lover_case = int(input("ile malych liter ma mieć hasło "))
update_charakter_left(lover_case)

upper_case = int(input("ile duzych liter ma mieć hasło "))
update_charakter_left(upper_case)

specjal_charakter = int(input("ile znaków specjalnych ma mieć hasło? "))
digits = int(input("ile cyfr ma mieć hasło "))
update_charakter_left(digits)

if charakter_left > 0 :
   
   print("haslo zostanie uzupełnione małymi literami")

   lover_case +=charakter_left

print()

print("Długość hasła",password_length)
print("małe litery",lover_case)
print("duze litery",upper_case)
print("znaki specjalne",specjal_charakter)

print("cyfry",digits)

for i in range(password_length):
   
   if lover_case>0:
      password.append(random.choice(string.ascii_lowercase))
      lover_case =-1

   if upper_case>0:
      password.append(random.choice(string.ascii_uppercase))
      upper_case =-1  

   if specjal_charakter>0:
      password.append(random.choice(string.punctuation))
      specjal_charakter =-1   
   
   if digits>0:
      password.append(random.choice(string.digits))
      digits-=1
      

random.shuffle(password)
print("wygenerowane hasło" ,"".join(password))
      

 

 

   

 




