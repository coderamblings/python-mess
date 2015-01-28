class Osoba:
    waga = 0
    imie = ''
    def przedstaw_sie(self):
        return 'dzien dobry, ' + self.imie
    def __init__(self):   # a tutaj upewniamy sie, ze konstruktor tworzy nowa liste na choroby, gdybysmy podali tylko choroby=[] pod waga, wszystkie instancje odwolywalyby sie do tego samego obiektu (przy liczbach nie ma tego problemu, kazda deklaracja tworzy nowy obiekt)
        self.choroby = []



o1 = Osoba()
o2 = Osoba()

o1.imie = 'Adam'
o1.waga = 87
o1.choroby.append('WZW A')
o1.choroby.append('pylica')

o2.imie = 'Bartek'
o2.waga = 65
o2.choroby.append('gruzlica')

print o1.przedstaw_sie()
