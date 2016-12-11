# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 01:26:26 2016

@author: Thomas

Oppgave:
I en fantasiverden skal en Trollmann, en Kriger, en Prest og en Tyv kjempe seg igjennom noen farlige tuneller og rom der en goblin-klan holder 17 mennesker fanget. Eventyrerene skal igjennom 100 rom før de finner fangene. I hvert rom må de nedkjempe eller snike seg forbi onde goblins. Det er like mange goblins i hvert rom som nummeret på rommet. Så i det første rommet er det en goblin, i det neste 2, osv frem til og med rom 100 der det er 100 goblins. Når de har kommet forbi rom 100 kan de befri fangene. I hvert rom går kampen i runder frem til det ikke er noen goblins igjen, etter følgende regler (i rekkefølge):

    Hvis Tyven er i live og det er goblins igjen i dette rommet, dreper han 1 goblin.
    Hvis Trollmannen er i live og det er goblins igjen i dette rommet, dreper han (opptil) 10 goblins.
    Hvis Krigeren er i live og det er goblins igjen i dette rommet, dreper han 1 goblin.
    Hvis Presten er i live og en annen eventyrer ikke er det, gjenoppliver presten en av de som ikke er i live. Hvis det er flere som ikke er i live velger han først Krigeren, så Trollmannen. Tyven vil han ikke gjenopplive, han har syndet for mye. Presten kan gjøre dette maks en gang per rom, og han kan ikke gjenopplive eventyrere som ble forlatt døde i et tidligere rom.
    Hvis Tyven er den eneste som er i live, sniker han seg videre (til neste rom eller til fangene hvis dette er rom 100), og ignorerer de goblinene som var igjen i dette rommet. Goblinene som var igjen i rommet leter etter ham, men går seg bort i tunellene og starter et nytt og bedre liv et annet sted.
    Hvis det fremdeles er både eventyrere og goblins i rommet, og det er minst 10 ganger flere goblins enn eventyrerene som er igjen, så dreper goblinene en av eventyrerene. De dreper først Krigeren om han er i live, deretter Trollmannen, så Presten. Tyven finner de ikke.
    Hvis det fremdeles er både eventyrere og goblins i rommet, gå til punkt 1 (ny runde i samme rom). Hvis ikke, gå til neste rom og start en runde - med mindre dette var det siste rommet, i hvilket tilfelle de resterende eventyrerene finner fangene og befrir dem.

Hvor mange overlevde historien?
"""

def survivors():
	survivors = 17
	heroes = ["thief", "priest", "wizard", "warrior"]
	for n in range(1,101):
		goblins = n
		deadInRoom = []
		resurrectedInRoom = False
		while goblins > 0:
			goblins -= 1
			if "wizard" in heroes:
				goblins -= 10
			if "warrior" in heroes:
				goblins -= 1
			if "priest" in heroes:
				if(resurrectedInRoom == False and len(deadInRoom) > 0):
							if "warrior" in deadInRoom:
								heroes.append(deadInRoom.pop(deadInRoom.index("warrior")))
								resurrectedInRoom = True
							elif "wizard" in deadInRoom:
								heroes.append(deadInRoom.pop(deadInRoom.index("wizard")))
								resurrectedInRoom = True
			if len(heroes) == 1 and "thief" in heroes:
				survivors += goblins
				break
			if goblins >= 10*len(heroes):
				deadInRoom.append(heroes.pop())
	survivors += len(heroes)
	print(str(survivors))

survivors()