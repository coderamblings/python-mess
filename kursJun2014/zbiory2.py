#!/bin/python

zestaw = set()

# tutaj dostaje listy do zbioru
# coach: p.sobolewski@alx.pl

#with open('dane3.txt') as plik:
#    for line in plik:
#        line = line.strip()
#        zestaw.add(str(line.split(';')))
#    
#print zestaw


# lepiej, zeyb kazde slowo dodac
with open('dane3.txt') as plik:
    for line in plik:
        line = line.strip()
        z2 = set((line.split(';'))) #wynik splita - lista
        zestaw = zestaw.union(z2)
print zestaw





