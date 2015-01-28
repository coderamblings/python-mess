
#start
#https://docs.python.org/2/library/xml.dom.html

p = xml.dom.minidom.parse('xml/pracownicy01.xml')
In [7]: print p
<xml.dom.minidom.Document instance at 0x2ccbb90>

#znajdujemy opis typu document w tej dokumentacji i znajdjemy
#https://docs.python.org/2/library/xml.dom.html#dom-document-objects
#zauwazamy, ze typ document dziedziczy po Node, warto sprawdzic co ma node

In [16]: print p.firstChild.__class__
xml.dom.minidom.Element

pr1.firstChild.getElementsByTagName('pracownik')[0]
primie = p.firstChild.getElementsByTagName('imie')[0]
#i dopiero tutaj dostajemy imie
print primie.firstChild.data

#lub krocej
print xml.dom.minidom.parse('xml/pracownicy01.xml').getElementsByTagName('imie')[0].firstChild.data

#inne narzedzie
import xml.etree.ElementTree
d = xml.etree.ElementTree.parse('xml/pracownicy01.xml')
#tutaj zapytanie XPAT'owe
il1 = d.findall('./pracownik/imie')[0]
print il1.text
#lub
il2 = d.findall("./pracownik[imie='Pantaleon']/nazwisko")[0]
print il2
print il2.text
#lub
d.findall("./pracownik[imie]/nazwisko")[0].text

#hint iconv -f utf-8 -t ascii//TRANSLIT <pracownicy08.xml -> zamienic ł na l
#przyklad dluzszego zapytania, tego juz ElementTree nie obsluguje
#print d.findall("./miasto[dzialy/dzial/pracownicy/pracownik[pesel=19031453254]]/nazwa"
