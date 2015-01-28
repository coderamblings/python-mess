#!/bin/python

for i in xrange(1,20,2):
    print str('*'*i).center(50,' ')
 
print " A z nozka?"

for i in range(1,40,2) + [3, 3, 3, 3]:
    print str('*'*i).center(50,' ')
# dodajemy sobie zakres 3 -> od 1 do 40 przez 2, a potem, 3, 3, 3, 3
#print range(1,40,2) + [3, 3, 3, 3]
#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 3, 3, 3, 3]

