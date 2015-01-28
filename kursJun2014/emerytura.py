
#wiek = raw_input ('Witaj, ile masz lat?')
#try:
#    pozostalo = 67 - int(wiek)
#except ValueError:
#    print 'Nie podales poprawnej liczby'
#else:    
#    print "Juz tylko", pozostalo, "lat do emerytury!"


wiek = None
while wiek == None:
#lub 'while wiek is None'
    try:
        wiek = int(raw_input ('Witaj, ile masz lat?'))
    except ValueError:
    	print 'Podaj liczbe przy pomocy cyfr!'
print "Juz tylko", 67 - wiek, "lat do emerytury!"


#funkcje wbudowane, np. dla stringow len(napis) - dlugosc, abs(liczba) - wartosc bezwzgledna
#poza tym, sa jeszcze metody, np. upper() dla stringow
#sa tez __add__ __mul__
#napis = 'Ola la la!'
#print napis.upper()
#print (a.__add__(b)).__mul__(c)  #( (a+b)*c)

