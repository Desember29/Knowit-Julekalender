# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:12:45 2016

@author: Thomas

Oppgave:
Finn det minste naturlige tallet som ender på 6 og som har følgende egenskap:
- hvis man fjerner det siste tallet og plasserer det først så blir tallet fire ganger så stort som det opprinnelige tallet.
"""

currentNumber = 6
found = False

while not found:
	originalNumber = str(currentNumber)
	lastNumber = originalNumber[-1]
	firstNumbers = originalNumber[:-1]
	invertedNumber = lastNumber+firstNumbers
	if (int(invertedNumber)%4 == 0):
		if ((int(invertedNumber)/int(originalNumber)) == 4):
			print(originalNumber)
			found = True
	currentNumber += 10