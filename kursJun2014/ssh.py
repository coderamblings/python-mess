import paramiko
transport = paramiko.Transport(('students.alx.pl', 22))
transport.connect(username='test', password='shaaM7mo')
transport.isAlive()

# tworzymy sesję, potem komenda, odczytujemy wynik, zamykamy sesję
sesja = transport.open_session()
sesja.exec_command('ls -lt')
print sesja.recv(1024) # tu podajemy liczbę bajtów, które pobieramy
print sesja.recv(1024) # kolejne 1024
print sesja.recv(1024) # kolejne 1024
transport.close()


# Alarm, jesli na zdalnym serwerze zajetosc na '/' wieksza niz 72%


import paramiko
transport = paramiko.Transport(('students.alx.pl', 22))
transport.connect(username='test',password='shaaM7mo')
transport.isAlive()
sesja = transport.open_session()
sesja.exec_command('df -h')
wynik = print sesja.recv(1024)
wynik = sesja.recv(1024)


re.findall('/$',wynik)
wlinie = wynik.split('\n')
wwlinie = wlinie[1].split()



for i in wlinie:
    if re.findall('/$',i):
        j = i.split()
        if int(str(j[4][:-1])) > 72:
            print 'warning!'


