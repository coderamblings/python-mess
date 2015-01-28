#!/bin/python
# Pobrac liste ip przez sftp, wczytac IP, spingowac wszystkie i wypisac, ktore odpowiadaja

import paramiko as p
import re
import subprocess

trans = p.Transport(('students.alx.pl', 22))
trans.connect(username='test', password='shaaM7mo')
sftp = p.SFTPClient.from_transport(trans)
pomiary = []

with sftp.open('ip.txt') as plik:
    for linia in plik:
        #znowu cos fajnego w regex, lapie IP
        if re.findall('(?:\d+\.){3}\d+', linia.rstrip()) :
            retcode = subprocess.call(['ping', '-c', '1', str(linia)])
            if retcode == 0:
                pomiary.append('Zyje: ' + linia.rstrip())
                #Nie pomiary = pomiary.append('Zyje: ' + linia.rstrip())
                #poniewaz pomiary.append nie zwraca zadnego wyniku, tylko dodaje element (nic nie zwraca, a wiec zwraca none), teraz to none przypisujemy do pomiary i klops
                print 'Nastepujacy host zyje:', linia

sftp.close()
print '\n'.join(pomiary)


#subprocess.call(['ping', '-c', '1', str(linia)], stdout=open(os.devnull), stderr=open(os.devnull))
# os.devnull --> wymaga import osl
#subpreocess.check_output --> jesli potrzebujemy tylko wyniku
