#kodowanie
# coding: utf-8
import sys

kodowanie_wyjscia = sys.stdout.encoding
if kodowanie_wyjscia is None:
    kodowanie_wyjscia = 'UTF-8'
napis = u'łódź'
print napis[:2].encode(kodowanie_wyjscia)
