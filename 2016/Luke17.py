# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 21:34:08 2016

@author: Thomas

Oppgave:
Ormehull
Du befinner deg i et rutenett som er 100.000x100.000 stort.

Du står i øvre venstre hjørnet av rutenettet, punktet 0,0, og skal til nedre høyre hjørne, punktet 99.999, 99.999. I rutenettet kan du bevege deg opp, ned, til høyre og til venstre. Hver bevegelse tar ett skritt. Hvis f.eks. fra start går ett skritt til høyre havner du på punktet 1,0. Hvis du så går ett skritt ned havner du på punktet 1,1 osv.

På rutenettet finnes det 11 ormehull som kan transportere deg fra ett punkt til et annet. Ormehullene fungerer begge veier, fra x til y og fra y til x og koster ingen skritt å bruke.
Ditt mål er å finne veien med kortest antall skritt til mål.

Eks:
Hvis rutenettet var 10x10 stort og det fantes 2 ormehull;
1,2-5,3
3,4-7,8

Ville antall skritt fra 0,0 til 9,9 være 9. F.eks. via. veien høyre, ned, ned, (ormehull fra 1,2 til 5,3), venstre, venstre, ned, (ormehull fra 3,4 til 7,8), ned, høyre, høyre.

Input: http://pastebin.com/raw/jTNGHzVe
"""

def findSteps():
	file = open("Luke17.txt")
	start = 0
	end = 99999
	wormholes = []
	for line in file:
		line = line.strip()
		line = line.split("-")
		wormhole = []
		for item in line:
			item = item.split(",")
			wormhole.append(int(item[0]))
			wormhole.append(int(item[1]))
		wormholes.append(wormhole)
	distances = []
	for wormhole in wormholes:
		toWormhole = abs(start - wormhole[0]) + abs(start - wormhole[1])
		fromWormhole = abs(wormhole[2] - end) + abs(wormhole[3] - end)
		distances.append([toWormhole, fromWormhole])
	sumDistances = []
	for distance in distances:
		sumDistances.append(sum(distance))
	print(min(sumDistances))

findSteps()