import re
import pymysql as m
import pymysql.cursors # konieczne, poniewaz cursors to modul a nie funckcja, a import modulu nie powoduje importu wszystkich podrzedbnych modulow


polaczenie = m.connect(host='127.0.0.1', user='psobolewski', passwd='nowehaslo', db='psobolewski', port=3306, cursorclass=pymysql.cursors.DictCursor) #dzieki temu zwrotki dostaniemy jako slownik a nie jako krotki
k = polaczenie.cursor()
k.execute('create table if not exists log3 (id serial primary key, ip varchar(20), operacja varchar(255))');

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
            operacja = z.group('operacja')
            k.execute('insert into log2 (ip, operacja) VALUES (%s, %s)', [ip, operacja])
            try:
                ipiki[ip] += 1
            except KeyError:
                ipiki[ip] = 1
k.connection.commit()
polaczenie.close()
