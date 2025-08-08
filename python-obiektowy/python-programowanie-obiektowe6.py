class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age


    def display_info(self):
        return f"name: {self.name} ,Age : {self.age}"
    
class Employee(Person):

    def work(self):
        return f"name: {self.name} is working as employee"
    
    
        
        




         

 