#!/bin/python

#zbiory --> nie maja duplikatow, kolejnosci
#i slowniki

import re



#ipiki = set() - zbior
ipiki = {}


with open('vsftpd.log') as plik:
    for linia in plik:
        z = re.search(r'''
^
\w\w\w\ (?P<miesiac>\w\w\w)               # miesiac
\ +(?P<dzien>\d+)                         # dzien
\ (?P<godzina>\d\d):(?P<minuta>\d\d):(?P<sekunda>\d\d)           # godzina
\ (?P<rok>\d\d\d\d)\                      # rok
\[pid\ \d+\]\                             #
(?:\[(?P<uzytkownik>[^\]]+)\]\ )?         # uzytkownik
(?P<operacja>[A-Z\ ]+):\ Client\          # operacja
"(?P<ip>(?:\d+\.){3}\d+)"(?:,\ )?         # ip
(?P<reszta>.*)$                           # reszta        
''', linia, re.VERBOSE)
        if z:
            miesiac = z.group('miesiac')
            ip = z.group('ip')
            try:
                ipiki[ip] += 1
            except KeyError:
                ipiki[ip] = 1
            
print '\n'.join(['%s:\t%d' % (k, ipiki[k]) for k in ipiki.keys()])
