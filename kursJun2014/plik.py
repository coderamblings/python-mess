#!/bin/python

#plik = open('data.txt')
# for linijka in plik:
#     print linijka
#plik.close()
#plik.readline()

suma = 0

with open('dane.txt') as plik:
    for linia in plik:
        try:
            
