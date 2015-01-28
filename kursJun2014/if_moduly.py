#!/bin/python
#zadanie: wypisac liczby o 1 do 100, jesli podzielna przez 3 slowo PIK, jesli przez 5 POK, jesli przez 3 i 5 to PIKPOK

for i in range(1,20):
    if (i % 3 == 0) and (i % 5 == 0):
	    print 'PIKPOK'
    elif (i % 3 == 0):
        print 'PIK'
    elif (i % 5 == 0):
        print 'POK' 	
    else:
		print i
