#-*-coding: utf-8-*-
import json
points = 0

def show_question(question):

    global points
 

    print(question["pytanie"])

    print("a:",question["a"])
    print("b:",question["b"])
    print("c:",question["c"])
    print("d:",question["d"])

    print()

    answer = input("która odpowiedz wybierasz: ")
   
    if answer == question["prawidlowa_odpowiedz"]:
     points+=1
     print(points)
    else: 
        
       points -= points
       print(points)


with open("python-zadania\quiz\plik.json") as json_file:
     questions = json.load(json_file)
    
     for index in range(0,len(questions)):
        show_question(questions[index])
 
if points<0:
   
   points= 0 
 
print('prawidlowe odpowiedzi ' , points)

