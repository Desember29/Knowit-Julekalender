# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 00:53:44 2016

@author: Thomas

Oppgave:
En skøyen alv har gjemt pakkene til nissen og julaften står i fare! Alven etterlot seg et kart over med et rødt kryss midt på finnmarksvidda med tekst 'start here'. På baksiden av kartet er det instruksjoner som sier hvor du skal gå fra krysset. Du har fått som oppgave å hjelpe nissen med å finne pakkene og redde julaften.

Skattekartet har veldig mange steg, men du ser kjapt at det bare består av 4 forskjellige instruksjoner, å gå x antall meter nord (north), sør (south), øst (east), eller vest (west). Du bestemmer deg for å lage et program som samler disse stegene og returnerer antall meter nord og antall meter vest, hvor et negativt tall betyr motsatt retning.

Eksempel:
walk 10 meters north
walk 10 meters south
walk 10 meters west
walk 10 meters east
walk 3 meters north
walk 2 meters east

gir resultatet:
3,-2

Skattekart: http://pastebin.com/BZrAMcN2 
"""

def instructionDecoder():
	file = open("Luke7.txt")
	distance = [0, 0]
	for line in file:
		words = line.split()
		if(words[3] == 'north'):
			distance[0] += int(words[1])
		elif(words[3] == 'south'):
			distance[0] -= int(words[1])
		elif(words[3] == 'west'):
			distance[1] += int(words[1])
		elif(words[3] == 'east'):
			distance[1] -= int(words[1])
	print(distance)

instructionDecoder()