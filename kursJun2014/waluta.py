#!/bin/python
# coding: utf-8

#znalezc kurs EUR z tabeli kursow NBP

import xml.etree.ElementTree

xml.etree.ElementTree.parse('xml/waluty.xml').findall('./pozycja[kod_waluty="USD"]/kurs_sredni')[0].text
