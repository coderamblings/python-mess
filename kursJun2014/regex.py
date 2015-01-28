#!/bin/python
# Zadanie: uzytkownik - podaj adres IP, a my sprawdamy, czy jest poprawny
import re

#kod = raw_input('Podaj kod pocztowy. Lub gin! ')
#if re.findall('^\d\d-\d\d\d$', kod, re.I):
#    print 'poprawny'
#else:
#    print 'Niepoprawny kod!'

#IP = raw_input('Podaj adres IP. Lub gin! ')
#if re.findall('^(?:\d|\d\d|\d\d\d)\.(?:\d|\d\d|\d\d\d)\.(?:\d|\d\d|\d\d\d)\.(?:\d|\d\d|\d\d\d)$', IP):
#    print 'Poprawny!'
#else:
#    print 'Niepoprawny!!'
    
# (?: ) - tylko match
# ( ) - wyciaga wskazany element

# miasto, ulica = re.findall(r'(\d\d)-(\d\d\d)', 'Moj kod pocztowy to 15-682') - zwraca wynik - liste krotek 2 elementami
# miasto, ulica = re.findall(r'(\d\d)-(\d\d\d)', 'Moj kod pocztowy to 15-682')[0] - zwraca wynik - jedna krotke z 2 elementami

#A teraz spytajmy o IP i sprawdzmy, czy jest dobre

IP = raw_input('Kup Pan IP cegle! ')
try:
    ip = re.findall('^(\d+)\.(\d+)\.(\d+)\.(\d+)$', IP)[0]
except IndexError:
    print 'go home!'
else:
    print ip
    if ip:
        print all([ int(x).bit_length() <= 9 for x in ip]) #all testuje, czy wszystkie elementy są True
                                                            
        #[int(x) for x in ip if int(x)>=0 and int(x)<256]
    else:
        print 'Nie pasuje'

# do przetrawienia:  liczby = 1,3,7,19 ; print [i > 5 for i in liczby]  => [False, False, True, True]
