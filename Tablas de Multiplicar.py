#! /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6
# -*- coding: utf-8 -*-

volver = "S"

while volver not in ("n", "N", "no", "No", "NO"):
	
	print ("Tablas")
	print ("##############################################################################")

	tab=int(input("Que tabla de multiplicar quieres que haga: "))
	hasta=int(input("Hasta que numero multiplico: "))

	for i in range(1, hasta+1): #<-- agrego 1 a hasta xq si no (hasta) es (hasta[real]-1)
		print (tab, "x", i, "=", tab*i)
		
	volver=(input("¿Quieres probar otra tabla? "))