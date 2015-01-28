#!/bin/python

#Przy pomocy lokalnego sendmaila = tworzymy wiadomosc, a potem pipe'm do procesu sendmail

from email.mime.text import MIMEText
import subprocess

#msg = MIMEText('czarna krowa w kropki bordo')
#print msg
#msg['Subject'] = 'masz wiadomosc'
#msg['From'] = 'jkowa@g.com'
#msg['To'] = 'fr@fr.com']
#sendmail = subprocess.Popen('[sendmail', '-t'], stdin=subprocess.PIPE)
#sendmail.communicate(str(msg))

#A teraz przy pomocy klienta SMTP
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
msg = 'Just a test message.'
s.ehlo()
s.starttls()
s.ehlo()
s.login('michal.frontczak@seamless.se', '')
s.sendmail('michal.frontczak@seamless.se', 'michal.frontczak@gmail.com', str(msg))
s.close()
