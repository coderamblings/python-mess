#!/bin/python

import paramiko as p
import re

t = p.Transport(('students.alx.pl', 22))
t.connect(username='test', password='shaaM7mo')

sftp = p.SFTPClient.from_transport(t)
sftp.get('other_vhosts_access.log', 'other_vhosts_access.log')

szukana_data = raw_input('Podaj date w formacie DD/Mie/RRRR ')

wzorzec = r'''
    \[
    (?P<data>\d+/[^/]+/\d\d\d\d)    # data - tutaj z definicja grupy!
    :(?P<godzina>\d\d):\d\d:\d\d       # godzina : minuta : czas
    \ [+-]\d\d\d\d          # strefa czasowa
    \]
'''
ile = 0
wzorzec = re.compile(wzorzec, re.VERBOSE)
with open('other_vhosts_access.log') as plik:
    for linia in plik:
        znalezione = re.search(wzorzec,linia)
        data = znalezione.group('data')
        godzina = int(znalezione.group('godzina'))
        if data == szukana_data and godzina >= 8 and godzina < 17:
            ile += 1
print 'Znalazlem %d polaczen' % ile # bajer, podmiana w tekscie wartosci, jak printf
