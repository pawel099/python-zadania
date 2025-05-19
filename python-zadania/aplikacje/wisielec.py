import sys

non_of_tries = 5
word = "kamil"
used_letters= []
user_word= []

def find_indexes(word,letter):
 
 indexes = []

 for index , letter_in_word in enumerate(word):
    
    if letter == letter_in_word:
       indexes.append(index)
 return indexes

for _ in word:
    user_word.append("_")

while True:

    letter = input("podaj literę: ")
    used_letters.append(letter)
    found_indexes = find_indexes(word,letter)

    if len(found_indexes)==0:
     
     print("nie ma takiej litery")
     non_of_tries-=1
     print("pozostało prób",non_of_tries)
    
    if non_of_tries==0:
      print("koniec gry")
      sys.exit(0)

    else:
     
     for index in found_indexes:
       user_word[index] = letter
       print(user_word)  

     if "".join(user_word) == word:
       print("Brawo to jest to słowo")
       sys.exit(0)
       
    print("uzyte litery" , used_letters)




 