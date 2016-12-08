# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:47:38 2016

@author: Thomas

Oppgave:
Finn kameleonen!

Noen personer har venner de egentlig hater, men fremdeles virker greie mot. Disse menneskene kalles for kameleoner. Din oppgave er å finne den største kameleonen i en venneflokk.

Forholdet mellom en person X og Y som definerer en kameleon X ser sånn ut:
1. Person X er venn med Person Y - dette forholdet er symmetrisk, så Y er nå også venn med X
2. Person X hater Person Y
3. Person Y hater ikke Person X

Altså, et forhold mellom 2 personer, hvor begge er venner, men den ene av dem hater egentlig den andre (ikke symmetrisk!).

Hvilken person (definert ved navn) har flest venner som han/hun egentlig hater?

Link til vennelista: http://pastebin.com/raw/e0bE4naA
"""

def main():
	file = open("Luke3.txt")
	relationshipList = []
	for line in file:
		createFriendsList(relationshipList, line.split())
	file.seek(0)
	for line in file:
		createHateList(relationshipList, line.split())
	return findLargestChameleon(relationshipList)


def createFriendsList(resultList, inputList):
	if (inputList[0] == "friends"):
		if (len(resultList) != 0):
			item1 = -1
			item2 = -1
			for x in range(0, len(resultList)):
				if(inputList[1] == resultList[x][0]):
					item1 = x
				elif(inputList[2] == resultList[x][0]):
					item2 = x
			if(item1 >= 0):
				resultList[item1][1].append(inputList[2])
			elif(item1 < 0):
				resultList.append([inputList[1], [inputList[2]], []])
			if(item2 >= 0):
				resultList[item2][1].append(inputList[1])
			elif(item2 < 0):
				resultList.append([inputList[2], [inputList[1]], []])
		else:
			resultList.append([inputList[1],[inputList[2]], []])
			resultList.append([inputList[2],[inputList[1]], []])

def createHateList(resultList, inputList):
	if (inputList[1] == "hates"):
		for x in range(0, len(resultList)):
			if (inputList[0] == resultList[x][0]):
				if (inputList[2] in resultList[x][1]):
					resultList[x][2].append(inputList[2])

def findLargestChameleon(inputList):
	currentLargestChameleon = None
	currentLargestChameleonFriendsHates = 0
	hates = []
	for person in inputList:
		currentPersonHates = 0
		for hates in person[2]:
			if (hates in person[1]):
				for person2 in inputList:
					if (hates == person2[0]):
						if (not(person[0] in person2[2])):
							currentPersonHates += 1
		if (currentPersonHates >= currentLargestChameleonFriendsHates):
			currentLargestChameleon = person[0]
			currentLargestChameleonFriendsHates = currentPersonHates
			print(person[2])
	return currentLargestChameleon, currentLargestChameleonFriendsHates
	
#list1 = [["Sarah", ["Justine", "Maria"], ["Maria"]],["Maria", ["Sarah"], ["Justine"]]]
#list2 = ["Sarah", "Maria"]

print(main())

#for item in list1:
#	if (list2[1] == item[0]):
#		item[1].append("Thomas")