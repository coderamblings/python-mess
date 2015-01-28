#!/bin/python
# napisac program czyta linie ponizej, zaczytac, a potem zmapowac elementy tej listy na float
#liczby = ['3.5', '2.7', '8.3']
#list comprehension - [wyrazenie for element in lista if warunek]

# MAPOWANIE

#floaty = [float(x) for x in liczby]
#print floaty[1]
#print sum(floaty)


#ile cyfr maja liczby od 0 do miliona?
#liczby = range(0,1000001)
#suma = 0
#stringi = [str(x) for x in liczby]
#for i in stringi:
#    suma += len(i)
#print suma

# krocej
#print 'Wynik wynosi %.2f' % sum([len(str(x)) for x in xrange(1000000+1)])

# Znajdzmy pierwsza liczbe ktorej suma cyfr wynosi 1410
# Zamienic liczby na liste stringow, potem poszczegolne strongi rozbic)
# lista jest iteracyjna, a int nie, dlatego zmieniamy na stringi najpierw, a potem znowu na inty, gdy dodajemy

#Najpierw uproszczone - policzmy sume cyfr 16514
#i = 16514 
#si = str(i)
#lsi = list(si) # tu od razu rozbicie na poszczegolne elementy
#print sum([int(x) for x in lsi])

#No dobra, no to suma cyfr co najmniej 20
# Wyswietlamy pare liczba - suma cyfr
#print ((liczba, sum(int([int(x) for x in list(str(liczba))) for liczba in xrange(101,129,)])

#I teraz jeszcze jedno cwiczenie z listami
ip = raw_input('Podaj IP')
port = raw_input('Podaj port')
with open('dane3.txt') as plik:
    czasy = (
        float(linia.split(';')[2].replace(',','.'))
        for linia in plik
        if linia.split(';')[0] == ip and linia.split(';')[1] == port
    )
    print min(czasy)
    print sum(czasy)
#tutaj minimum znajdujemy, ale nie znajdziemy sumy, bo juz przeszlismy przez cala liste...
