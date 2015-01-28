#!/bin/python
# zadanie: pytac 'podaj liczbe' az uzytkownik poda 'koniec', wtedy wypisac sume

suma = 0
while True:
    wiek = raw_input('Podaj liczbe ')
    #if wiek.lower() == 'koniec':
    #    break
    try:
        suma += int(wiek)
    except ValueError:
        print 'Koniec to nie liczba'

print "Suma tychze liczb: ", suma

#LUB

#while i != 'koniec'
#    i = raw_input('Dawaj liczbe')
#    if i != 'koniec':
#        suma = += int(i)
#print suma
