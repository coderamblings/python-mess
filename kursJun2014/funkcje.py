#!/bin/python

# szybkie funkcje

simply = lambda a, b: a(b+1)


def(a):
    return a * 3


def f(a, b):
    if b is None:
        return a * 3
    else:
        return a + b

print f(3)

# Note - jezeli gdziekolwiek w funkcji jest deklaracja lokalnej zmiennej, to wszedzie w tej funkcji odwolujemy sie do zmiennej lokalnej - nawet, jesli najpierw jest odwolanie do globalnej, a potem do lokalnej - co moze zwrocic blad , ze lokalna nie jest jeszcze zadeklarowana

# Zeby odwolywac sie tylko do zmiennej globalnej, w ciele funkcji deklarujemy
# global <variable>

# W funkcji nie mozemy zmieniać referencji, czyli ponownie zadeklarowac tej samej zmiennej. Natomiast mozemy modyfikowac listy, zbiory itd, bo referencja jest taka sama, tylko obiekt jest modyfikowany

# Note - kazdy modul ma wlasne zmienne globalne, wlasny scope

#Tu ponizej - print wyswietla 3,5,7, poniewaz x przejmuje referencje do tej samej listy, na ktora wskazuje a, "a" zostanie zmodyfikowane
def f(x):
    x.append(7)

a = [3, 5]
f(a)
print a

#opis funkcji - ciele, np.
def f2(a):
    'Tralala, jak dziala ta funkcja'
    a = a**3

# Importowanie:
# import <modul> - daje mozliwosc odniesienia sie do funkcji przez <modul>.<funkcja>
# from <modul> import <funkcja> - daje mozliwosc odniesienia sie do funkcji przez <funkcja>
