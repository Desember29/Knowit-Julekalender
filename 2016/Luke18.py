# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 11:30:04 2016

@author: Thomas

Oppgave:
Du befinner deg i et rom der den eneste lyskilden er en gammel digital vekkerklokke (det er ingenting annet som gir lys i rommet enn denne). Sifrene på vekkerklokka er LEDs organisert i et såkalt 7-segments display. Klokkevisningen er på formatet hh:mm:ss, og er konfigurert opp til å vise klokkeslettet i 24 timersformat. Det første sifferet i timevisningen er blankt om tallet på timeplassen er mindre enn 10.

Anta at alle LEDene bidrar like mye til lysstyrken i rommet. Hvor lang tid går det fra rommet er på sitt mørkeste til det er på sitt lyseste? Svaret oppgis på formatet hh:mm:ss.

Eksempel: Tar dette 3 timer og 15 minutter og 3 sekunder blir svaret 03:15:03
"""

import datetime

LEDValues = {"0": 6, "1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6}

def minLEDs(LEDValues):
	hours = None
	rest = None
	currentLEDs = 8
	for x in range(0, 24):
		if x < 10:
			if LEDValues[str(x)] == currentLEDs:
				hours = x
			elif LEDValues[str(x)] < currentLEDs:
				hours = x
				currentLEDs = LEDValues[str(x)]
		else:
			string = str(x)
			LEDs = 0
			for char in string:
				LEDs += LEDValues[char]
			if LEDs == currentLEDs:
				hours = x
			elif LEDs < currentLEDs:
				hours = x
				currentLEDs = LEDs
	currentLEDs = 8
	for y in range(0, 60):
		string = str(y)
		if y < 10:
			string = "0" + string
		LEDs = 0
		for char in string:
			LEDs += LEDValues[char]
		if LEDs == currentLEDs:
			rest = y
		elif LEDs < currentLEDs:
			rest = y
			currentLEDs = LEDs
	return hours, rest

def maxLEDs(LEDValues):
	hours = None
	rest = None
	currentLEDs = 0
	for x in range(0, 24):
		if x < 10:
			if LEDValues[str(x)] == currentLEDs:
				hours = x
			elif LEDValues[str(x)] > currentLEDs:
				hours = x
				currentLEDs = LEDValues[str(x)]
		else:
			string = str(x)
			LEDs = 0
			for char in string:
				LEDs += LEDValues[char]
			if LEDs == currentLEDs:
				hours = x
			elif LEDs > currentLEDs:
				hours = x
				currentLEDs = LEDs
	currentLEDs = 0
	for y in range(0, 60):
		string = str(y)
		if y < 10:
			string = "0" + string
		LEDs = 0
		for char in string:
			LEDs += LEDValues[char]
		if LEDs == currentLEDs:
			rest = y
		elif LEDs > currentLEDs:
			rest = y
			currentLEDs = LEDs
	return hours, rest

def findDuration(LEDValues):
	startHour, startRest = minLEDs(LEDValues)
	endHour, endRest = maxLEDs(LEDValues)
	if startRest < 10:
		startRest = "0" + str(startRest)
	if endRest < 10:
		endRest = "0" + str(endRest)
	startTime = datetime.datetime(2016, 12, 24, startHour, int(startRest), int(startRest))
	endTime = datetime.datetime(2016, 12, 24, endHour, int(endRest), int(endRest))
	difference = endTime - startTime
	return difference
	
	
print(findDuration(LEDValues))
