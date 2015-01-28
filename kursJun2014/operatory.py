#!/bin/python
#operator "trynarny", tj. przyjmujacy wiecej niz 2 parametry
#a = 3
#b = 12 if a > 3 else 34

#wiek = raw_input("Ile masz lat?" )
#wiadomosc = 'Jestes pelnoletni' if int(wiek) >= 18 else 'Jestes niepelnoletni'
#print wiadomosc

#krocej
wiek = int(raw_input("Ile masz lat?" ))
print 'Jestes', ("nie" if wiek < 18 else '') + 'pelnoletni.'
