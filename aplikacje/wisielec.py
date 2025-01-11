# znajdz bład w programie 

import sys

non_of_tries = 5
word = "pawel"
 

used_letters = []
user_word = []
 

def find_indexes(word,letter):
    indexes = []
    for index,letter_in_word in enumerate(word):
     if letter == letter_in_word:
        indexes.append(index)

    return indexes 
 
for _ in word:
    
    user_word.append("_")

while True:

    letter = input('Podaj litere: ')
    used_letters.append(letter)
    found_indexes = find_indexes(word,letter)

    if len(found_indexes)==0:
     
      print("nie ma takiej litery")
      non_of_tries-=1

      if non_of_tries==0:
         print("koniec gry")
         sys.exit(0)

       
    print("uzyte litery" ,used_letters)




     


