# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 16:17:12 2016

@author: Thomas

Oppgave:
Å nei, i julestresset har Alvin glemt det eneste han skulle huske hele julen; det hemmelige tallet!
Det eneste han husker er at tallet er det høyeste mulige produktet hvis du multipliserer to tall som består av sifrene 0-9 hvor man bare kan bruke hvert siffer én gang.

F.eks er dette to gyldige tall å multiplisere: 12340 * 56789, mens dette er ikke to gyldige tall å multiplisere: 220135 * 74896

Hva er det hemmelige tallet Alvin har glemt?
"""

def findHighestProduct():
	numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	#Numbers have to go from highest number to lowest number in order to have the highest product
	leftNumber = str(numbers.pop())
	rightNumber = str(numbers.pop())
	while len(numbers):
		if int(leftNumber) < int(rightNumber):
			leftNumber = leftNumber + str(numbers.pop())
		else:
			rightNumber = rightNumber + str(numbers.pop())
	print(int(leftNumber) * int(rightNumber))

findHighestProduct()