#!/bin/python
#napis = 'hilton'
#for litera in napis:
#    print litera
#print 'koniec'
#ipython --> help (type), np help (str)

#dlugosc = raw_input('Podaj cyfry')
#for digit in dlugosc:
#    print "x"*int(digit)


#boolean - owszem, ale musza byc zdefiniowane z wielkiej, a = True
#stringi mozna wywolywac albo printem albo bezposrednio
napis = "trlalala\nlalamido"
print str(napis)
print repr(napis)

a = 3, 5, 7 #krotka - pythonie nie ma tablic! krotki sa niezmienialnie, podobnie jak stringi
#trick - jak chcemy odpytać o pomoc o typie zmiennych, a nie pamietamy, jak się nazywa ten typ?
#zdefiniowac zmienna, potem print type(var), potem help(type)

print '---'.join(a) #wyswietli a, laczac elementy '---'

b = [1, 3, True, 'baza', (3,5)] #lista - rozni sie od krotki tym, ze jest zmianialna
