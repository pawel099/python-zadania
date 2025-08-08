#-*-coding: utf-8-*-
import json
points = 0

def show_question(question):
 

    print(question["pytanie"])

    print("a:",question["a"])
    print("b:",question["b"])
    print("c:",question["c"])
    print("d:",question["d"])

    print()

    answer = input("która odpowiedz wybierasz: ")
   
    if answer == question["prawidlowa_odpowiedz"]:
     print("To prawidłowa odpowiedz ")

    else: "niestety nie odgadłeś"   


with open("python-zadania\quiz\plik.json") as json_file:
     questions = json.load(json_file)
    
     for index in range(0,len(questions)):
        show_question(questions[index])





