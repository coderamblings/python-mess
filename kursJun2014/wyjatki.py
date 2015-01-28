#
a = 3
b = 0

try: 
    c = a / b
except ZeroDivisionError:
    print 'B00m!'
else:
    #jak try nie rzuci wyjatku, to jeszcze to rob
finally:
    #finally rob zawsze
    print ' I tak to wyswietlimy.'

print 'Booyah!'

#except bez okreslenia wyjatku - lapie wszystkie
#jak juz wstawimy try - musi byc except, ew. "except pass"
