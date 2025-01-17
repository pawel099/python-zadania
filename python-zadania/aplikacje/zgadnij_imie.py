def zgadnijImie():

 imie = None
 licznik =0

 while imie!= 'pawel':

    imie = input("jak masz na imię ? ")
    licznik +=1

 return licznik

r = zgadnijImie()

print("brawo odgadłeś za " ,r ,"razem ")