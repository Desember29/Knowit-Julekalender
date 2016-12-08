# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 10:54:51 2016

@author: Thomas

Oppgave:
Kongen av Indonesia har som tradisjon å sende sine julehilsener kryptert til sine venner. I år skjedde det en glipp og kongen sendte meldingen til alle i hele verden med en email adresse, vi har også fått meldingen og trenger hjelp til å dekryptere den. Med meldingen fulgte også følgende instruksjoner på hvordan den kan dekrypteres:

For å dekryptere meldingen må man først legge sammen parene i listen, ett par er første og siste element, andre og nest siste element og så videre. Når du har alle verdiene kan du oversette disse til bokstaver, hvor a = 1 og z = 26.
Kryptertmelding: http://pastebin.com/xfX3msCL
"""

romanNumeralValue = {"0": 0, "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13}

def createNumberList():
	file = open("Luke5.txt")
	data = file.readline()
	splitData = data.split(",")
	numbersList = []
	for item in splitData:
		if "[" in item:
			string = item.replace("[", "")
			string = string.strip()
		elif "]" in item:
			string = item.replace("]", "")
			string = string.strip()
		else:
			string = item
			string = string.strip()
		numbersList.append(romanNumeralValue[string])
	return numbersList

def addNumbers(inputList):
	resultList = []
	while len(inputList) > 0:
		firstNumber, secondNumber = inputList.pop(0), inputList.pop()
		resultList.append(firstNumber+secondNumber)
	return resultList

def decodeMessage(inputList):
	message = ""
	while len(inputList) > 0:
		message += chr(inputList.pop(0)+96)
	return message

def main():
	return(decodeMessage(addNumbers(createNumberList())))
	
print(main())