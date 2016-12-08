# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:24:49 2016

@author: Thomas

Oppgave:
Fibonaccirekken er en tallrekke som genereres ved at man adderer de to foregående tallene i rekken. f.eks. om man starter med 1 og 2 blir de første 10 termene 1, 1, 2, 3, 5, 8, 13, 21, 34 og 55
Finn summen av alle partall i denne rekken som er mindre enn 4.000.000.000
"""


from math import sqrt
def F(n):
	return (round(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))))

def summationOfEvenFibonacci():
	sumOfEvenFibonacci = 0
	n = 0
	Fn = F(n)
	while (Fn < 4000000000):
		if ((Fn%2) == 0):
			sumOfEvenFibonacci += Fn
		n += 1
		Fn = F(n)
	return (sumOfEvenFibonacci)

print(summationOfEvenFibonacci())