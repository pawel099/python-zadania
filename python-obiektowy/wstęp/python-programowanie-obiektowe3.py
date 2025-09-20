# metody
class person:
    def __init__(self,name):
         self.name = name

    def __str__(self):
          return 'nazywam się' + ' ' + self.name 
          
    def great(self):
         print('witaj' + ' ' + self.name)
    
    def farewall(self):
         print('zegnaj' + ' ' + self.name)

persons = person('alik')
print(persons)
obj_str = str(persons)

if persons.great() != None:
 print(persons.farewall())
 
 
 



