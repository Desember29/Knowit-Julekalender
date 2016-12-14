# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 07:34:56 2016

@author: Thomas

Oppgave:
I påvente av hva som kan skje når Trump inntar presidentstolen, har Knowit begynt å regne på noen passende mot-tiltak. Den amerikanske regjeringen har allerede utredet mulighetene for å bygge en Death Star, og selv om Obama-administrasjonen sa nei til The Death Star Petition i 2012 så tror vi det er meget sannsynlig at Trump kommer til å bestille en. Energien i strålen fra en Death Star må nå ca 2.25 * 10^32 J for å ødelegge jorden [Boulderstone et al. 2011].

Knowits ingeniører har funnet ut at for å stoppe dette trenger vi en legering bestående av et partall antall metaller. Det kan maks være 16 metaller med i legeringen. Metallene det er snakk om er for øyeblikket ikke kjent for andre enn forskerne i Area 51 og oss i Knowit. Dere kan kalle dem metall-1, metall-2 osv opp til metall-16.

Metallene har en planet-killer-motstandskraft lik tallet opphøyd i seg selv (så metall 1 har en motstandskraft på 1, metall 16 har en motstandskraft på 16^16. Motstandskraften til en legering er produktet av kraften til metallene som er med i legeringen.

Så legeringen bestående av metall-2 og metall-4 vil ha en motstandskraft lik produktet av motstanden i metall-2 og metall-4. Det blir (2^2) * (4^4), eller 4*256 = 1024.

Finn metallene i den legeringen som har mostandskraft høyere enn energien som skal til for å ødelegge jorden, hvor summen av fakultetsverdiene av nummrene på metallene i legeringen er lavest mulig. For eksempel, om kandidatene er legeringen bestående av metall 13 og 14, eller metall 11 og 15, så må du sammenligne 13!+14! med 11!+15! og velge legeringen med lavest resultat.

Svaret vi er ute etter er numrene på metallene som er med i legeringen konkatenert i stigende rekkefølge (ikke i kommaseparert liste).

Eksempel: viser det seg at alt du trenger er elementene 1 og 16 i legeringen blir svaret 116.

Help us! You're our only hope! (You're all rebels, aren't you?)
"""
from math import factorial
import itertools

def alloy():
	energy = 2.25 * 10**32
	alloyStrengths = dict()
	for n in range(1, 17):
		alloyStrengths[str(n)] = n**n
	subsets = []
	for l in range(0, len(alloyStrengths)+1):
		for subset in itertools.combinations(alloyStrengths, l):
			subsets.append(subset)
	criteriaMatch = []
	for subset in subsets:
		s = 1
		for item in subset:
			s = s*alloyStrengths[item]
		if s > energy:
			criteriaMatch.append(subset)
	lowestSubset = None
	lowestFactorialSum = 8212685046336
	for subset in criteriaMatch:
		factorialSum = 0
		for item in subset:
			factorialSum += factorial(int(item))
		if factorialSum < lowestFactorialSum:
			lowestFactorialSum = factorialSum
			lowestSubset = subset
	temp = []
	for item in lowestSubset:
		temp.append(item)
	if(len(temp)%2 != 0):
		if(not "1" in temp):
			temp.insert(0, "1")
	temp.sort()
	string = ""
	for n in range(len(temp)):
		string += temp[n]
	print(string)

	
		

alloy()

"""def subset_sum(numbers, target, partials, partial=[]):
	s = 1
	for item in partials:
		s = s*item
	if s > target:
		partials.append(partial)
		print(partials)
		return
	for i in range(len(numbers)):
		n = numbers[i]**numbers[i]
		remaining = numbers[i+1:]
		subset_sum(remaining, target, partials, partial + [n])

subset_sum(range(1,17), 2.25 * 10**32, partials)
print(partials)"""