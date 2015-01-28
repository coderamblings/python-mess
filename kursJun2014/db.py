# coding: utf-8
# info w jakim kodowaniu jest ten plik


#trans = p.Transport(('students.alx.pl', 22))
#trans.connect(username='test', password='shaaM7mo')

#db psobolewski nowehaslo

import pymysql as m
# Tutaj zakladamy, ze albo laczymy sie do localhosta, albo do tunelu, ktory zestawilismy, trzeba podac host=IP, inaczej klient sprobuje polaczyc sie po sockecie

polaczenie = m.connect(host='127.0.0.1', user='psobolewski', passwd='nowehaslo', db='psobolewski', port=3306)
k = polaczenie.cursor()
k.execute('SET NAMES UTF8') # w jakim wyniku chcemy wyniki
k.execute('select imie, nazwisko, kraj from zawodnicy')
wynik = k.fetchall()
for wiersz in wynik:
    print wiersz[0] #lista pierwszego elementu krotek

for wiersz in wynik:
    print wiersz  #lista krotek

#a propos
napis = u'łódź' #tu mamy ciag bajtow
type (napis) #juz nie jest to string, lecz unicode!
#konwersja
napis = napis.decode('UTF-8')   #tu jest ciag liter
napis = napis.encode('UTF-8')   #tu z powrotem zmieniamy litery na bajty (zgodnie z UTF8)
#to jest konieczne np. gdy chcemy przekierowac output programu, majac polskie znaki - bo standardowo python uzywa ASCII i przekierowanie sie wywala, bo python probuje UTF8 logowac przy pomocy ASCII i jest blad

#k.scroll(N) - przewijanie cursora, przydatne przy k.fetch

i = len(wynik)
j = len(wiersz)

#teraz wyswietlic na szybko:
for wiersz in wynik:
    #i = 0
    print ' '.join(wiersz)

# alternatywa -    
#for wiersz in wynik:
# - for i in wiersz: - tylko pamietac, ze tutaj w wiersz i i nie trafiaja intiger, tylko kolejne elementy iterabla
        #j = 0
        
        #j +=1
    #i =+ 1
        
#i jeszcze inne, jak dodac zmienna do kwerendy
kraj = raw_input('Bla')
k.execute('SELECT * FROM zawodnicy WHERE kraj="' + kraj + '"')
# problem tutaj - umozliwia SQL injection
#import pymysql
#In [2]: pymysql.paramstyle
#Out[2]: 'format'
# teraz sprawdzamy w dokumentacji pymysql, jak odnosic sie do parametrow 'format', tam stoi, ze %s
k.execute('SELECT * FROM zawodnicy WHERE kraj = %s', [kraj])
