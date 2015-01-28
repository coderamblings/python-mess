#!/bin/python
#napisac modul o nazwie mail, z funkcja sendd, ktorej podajemy, co trzeba, a ona wysyla maila

from email.mime.text import MIMEText
import subprocess
import smtplib


def sendd(nadawca, haslo, odbiorca):

    s = smtplib.SMTP('smtp.gmail.com', 587)
    msg = 'Just a test message.'
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(nadawca, haslo)
    s.sendmail(nadawca, odbiorca, str(msg))
