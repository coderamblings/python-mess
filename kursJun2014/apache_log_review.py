#!/bin/python

# grab an Apache log file, user provides date, we provide number of connections from 8-17

import re

#zrodlo = 'other_vhosts_access.log'

#data = raw_input('Podaj date w formacie DD/Mie/RRRR ')
sconn = 0


#with open(zrodlo) as plik:
#    for linia in plik:
#        try:
#            #conn = re.findall('\d\d/\[A-Z]\w\w/\d\d\d\d')
#            conn = re.findall(data + ':(?:0[8-9]|1[0-7])',linia)
#            if conn:
#                sconn += 1
#        except:
#            pass
#plik.close()

#V2

szukana_data = raw_input('Give ')
#wzorzec = r'''
#    \[
#    (\d+/[^/]+/\d\d\d\d)    # data
#    :(\d\d):\d\d:\d\d       # godzina : minuta : czas
#    \ [+-]\d\d\d\d          # strefa czasowa
#    \]
#'''
#ile = 0
#wzorzec = re.compile(wzorzec, re.VERBOSE)
#with open(zrodlo) as plik:
#    for linia in plik:
#       data, godzina = re.findall(wzorzec,linia)[0] # VERBOSE -- ignoruje white spaces, pozwala w polaczeniu z ''' na rozbijanie regexa jak wyzej [0] na koncu - da nam krotke jako wynik, zamiast listy krotek
#       godzina = int(godzina)
#       if data == szukana_data and godzina >= 8 and godzina < 17:
#           ile += 1
#print 'Znalazlem %d polaczen' % ile # bajer, podmiana w tekscie wartosci, jak printf

#V3 z grupami oraz z sciaganiem z URL'a

wzorzec = r'''
    \[
    (?P<data>\d+/[^/]+/\d\d\d\d)    # data - tutaj z definicja grupy!
    :(?P<godzina>\d\d):\d\d:\d\d       # godzina : minuta : czas
    \ [+-]\d\d\d\d          # strefa czasowa
    \]
'''

import urllib2

plik = urllib2.urlopen('http://psobolewski.students.alx.pl/tmp/other_vhosts_access.log')
#poniewaz juz tutaj robimy open, mozemy w ogole wywalic open(sciezka) as plik

ile = 0
wzorzec = re.compile(wzorzec, re.VERBOSE)
    for linia in plik:
       znalezione = re.search(wzorzec,linia)
       data = znalezione.group('data')
       godzina = int(znalezione.group('godzina'))
       if data == szukana_data and godzina >= 8 and godzina < 17:
           ile += 1
print 'Znalazlem %d polaczen' % ile # bajer, podmiana w tekscie wartosci, jak printf
