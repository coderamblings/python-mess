#!/bin/python

#Zadanie - odpytaj o imie i wyswietl je, ale zamien pierwsza litere na 'O'

imie = raw_input('Imie?')

nowe_imie = list(imie)
nowe_imie[0] = 'O'
print "Czesc", ''.join(nowe_imie)


# LUB
print 'or in another way'
print 'Czesc O' + imie[1:]

# range vs xrange --> range tworzy obiekty do ktorych mozna sie odwolac, a xrange nie - przez to xrange nie zajmuje pamieci
# xrange - tylko iterator
