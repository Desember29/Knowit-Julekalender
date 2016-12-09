# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 13:26:19 2016

@author: Thomas

Oppgave:
I en cryptocurrency som f. eks. Bitcoin bestemmes balansen til en konto ut av historikken av transaksjoner. Det vil si at hvis historikken kun består av én transaksjon hvor addresse X mottok 10 penger, så sier vi at balansen til X er 10.Dersom det kommer en ny transaksjon fra X til Y hvor det sendes 7 penger, så er balansen til Y: 7 og X: 3.

I filen det lenkes til finnes det to typer transaksjoner. Den ene typen er som den første beskrevet her, hvor penger trykkes ut av intet, og en heldig adresse mottar en viss sum penger. I den andre typen går pengene fra en adresse til en annen.

Ved å holde rede på alle transaksjoner i filen http://pastebin.com/raw/2vstb018, hvor mange adresser har en balanse på mer enn 10 penger når samtlige transaksjoner er utført?

Alle transaksjoner er gyldige, så du slipper å validere dem.

Formatet i filen er:

    None,9251b282-e1bc-4221-80d8-36b25826ebac,50

    9251b282-e1bc-4221-80d8-36b25826ebac,73b2dc61-24f4-4b0b-aca6-8c2d50b0e66c,38


Linje 1 sender 50 penger fra None til 9251b282-e1bc-4221-80d8-36b25826ebacLinje 2 sender 38 penger fra 9251b282-e1bc-4221-80d8-36b25826ebac til 73b2dc61-24f4-4b0b-aca6-8c2d50b0e66c
"""

def transactions():
	file = open("Luke9.txt")
	accounts = dict()
	for line in file:
		line = line.split(",")
		if(line[1] in accounts):
			accounts[line[1]] += int(line[2])
			if not (line[0] == "None"):
				accounts[line[0]] -= int(line[2])
		else:
			accounts[line[1]] = int(line[2])
			if not (line[0] == "None"):
				accounts[line[0]] -= int(line[2])
	counter = 0
	values = accounts.values()
	for value in values:
		if(value > 10):
			counter += 1
	print(counter)
				
			



transactions()