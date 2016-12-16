# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 12:09:55 2016

@author: Thomas

Oppgave:
Julenissen er glad i å leke med tall og å kombinere det med en gjettelek er alltid en slager. I dagens luke tenker han på et sekssifret tall hvor summen av sifrene er 43. Og hvor bare to av de tre påstandene under er sanne:

    det er et kvadratisk tall
    det er et kubisk tall
    tallet er mindre enn 500 000


Hvilket tall er det Julenissen tenker på?
"""

def number():
	n = 100000
	number = None
	while n < 500000:
		if ((n**(1. /2)).is_integer()):
			if(sum(map(int, str(n))) == 43):
				number = n
		n += 1
	print(number)

number()