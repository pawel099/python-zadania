#strukturyzacja kodu 

class Adress:
 def __init__(self,street:str,streat_number:int,postal_code:str,city:str):
  
  self.street = street
  self.street_number = streat_number
  self.postal_code = postal_code
  self.city = city


class Flat:
 def __init__(self,adress:Adress,size:float,rooms:int):
  
  self.adress = adress
  self.size = size
  self.rooms = rooms  


adress1 = Adress(
  'woronicza',
  '50',
  '02-657',
  'poznań'

  
  )

adress2 = Adress(
  'marzanny',
  3,
  '02-649',
  'Warszawa'
  
  )


flat = Flat(adress2,100,10)

print(flat.adress.city)




 
 
