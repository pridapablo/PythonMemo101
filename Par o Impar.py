#! /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6
# -*- coding: utf-8 -*-

volver="s"

while volver not in ("n", "N", "no", "No", "NO"):
	
	num1=int(input("Dime un numero entero (primer termino del rango) "))
	num2=int(input("Dime un numero mayor o igual al anterior (último termino del rango -1) "))

	print ("PARES O IMPARES")
	if num1>=num2:
		print ("Te dije mayor o igual al primero")
	else:
		for i in range(num1,num2+1):
			if i%2==0: #<-- se refiere al residuo (moulo) de ("i÷2")
				print (i, "es par")
			else:
				print (i, "es impar")
				
	volver=(input("¿Quieres probar otros numeros? "))
