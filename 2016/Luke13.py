# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 10:15:28 2016

@author: Thomas

Oppgave:
Hvert år greier naboen din å slå deg i årets juledekorasjon. Dette er noe du ikke finner deg i lengre og du har dermed gått drastisk til verks og kjøpt inn hundre millioner LED lys som er satt sammen i et 10.000x10.000 rutenett.

Julenissen har vært ganske snill med deg i år, så han har faktisk sendt deg de beste instruksjonene for hvordan å styre rutenettet med LED lys. Men hvordan fungerer virkelig dette?

LEDs i rutenettet ditt er nummerert fra 0 til 9999 i hvert retning, det vil si at hjørnene angis ved:

    0,0 - øverst til venstre
    0,9999 - nederst til venstre
    9999,9999 - nederst til høyre
    9999,0 - øverst til høyre

Instruksjonene har tre forskjellige måter å justere lysene på, "turn on", "turn off", "toggle" med koordinater for hvilke LEDs som skal endres.

Dette året skal du vinne konkurransen! For å greie dette trenger du kun å følge instruksjonene til julenissen og gjøre det i riktig rekkefølge.

Eksempler på hver linje av inputs:
turn on 0,0 through 9999,9999 kommer til å slå på (eller la de stå på) alle lys
toggle 0,0 through 9999,0 vil veksle første rad med 10000 lys
turn off 0,0 through 4999,4999 kommer til å slå av (eller la de være av) lysene i det rutenettet

Obs: Hvert koordinatpar representerer motsatt hjørne av et rektangel, som vil si at et par av koordinater 0,0 til 2,2 betyr 9 LEDs i et 3x3 firkant. Alle LEDs starter med å være slått av.

Eksempel på endring av lys:
Før endring:
0,0,0
0,0,0
0,0,0

turn on 0,0 through 1,1

Etter endring:
1,1,0
1,1,0
0,0,0

Etter å ha fulgt instruksjonene, hvor mange lys er på?
Input: http://pastebin.com/raw/aTeSBwR4
"""
from numpy import zeros

def christmasLights():
	lights =  zeros((10000, 10000), dtype=int)
	counter = 0
	file = open("Luke13.txt")
	for line in file:
		line = line.replace(",", " ")
		line = line.replace("through ", "")
		line = line.replace("turn ", "")
		line = line.split()
		xList = [int(line[1]), int(line[3])]
		yList = [int(line[2]), int(line[4])]
		operation = line[0]
		if(xList[0] <= xList[1] and yList[0] <= yList[1]):
			for y in range(yList[0], yList[1]+1):
				for x in range(xList[0], xList[1]+1):
					if operation == "toggle":
						if lights[y][x] == 0:
							lights[y][x] = 1
							counter += 1
						elif lights[y][x] == 1:
							lights[y][x] = 0
							counter -= 1
					elif operation == "on" and lights[y][x] != 1:
						lights[y][x] = 1
						counter += 1
					elif operation == "off" and lights[y][x] != 0:
						lights[y][x] = 0
						counter -= 1
	file.close()
	print(str(counter))

christmasLights()