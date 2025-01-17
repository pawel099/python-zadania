print("wyszukaj liczbę pierwszą")

def checkPrimeNumber(number):
    for dane in range(2,number):
      
      if number%dane == 0 :
        return "bład"
      else:
       return "liczba pierwsza!"    
         
inputs = int(input("podaj dowolną liczbę: "))
outs = checkPrimeNumber(inputs)

if outs==None:
 print("bład")

else:
 print(outs)