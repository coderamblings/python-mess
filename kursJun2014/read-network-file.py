#!/bin/python
# user podaje adres IP & port, program zwraca ilosc polaczen i czas polaczen, min, max, sredni

IP = raw_input('Podaj IP ')
czas = []

with open('network-data.csv') as input:
    for linia in input:
        linia = linia.rstrip()
        #obetnij white spaces po prawej stronie stringa
        if linia.split(',')[0] == IP:
        #niezly bajer -- zamieniamy linie na krotke i od razu odnosimy sie do jej pierwszego elementu (bo linia zawiera wszystko)
            dane = linia.split(',')
            czas.append(float(dane[2])) #od razu konwersja do float'a, zeby wyciagac srednie
        
print 'Czas minimalny: ', min(czas)
print 'Czas maksymalny: ', max(czas)
print 'Suma polaczen: ', sum(czas)
print 'Sredni czas polaczen: ', sum(czas)/len(czas)


# MAPOWANIE

#liczby = range (7)
#kwadraty = [x ** 2 for x in liczby] # i tu jeszcze można dodać if x < 5
## ** 2 - kwadrat, ** 3 - do potegi 3
## x jest tu wybrane przez nas

