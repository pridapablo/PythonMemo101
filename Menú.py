#! /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6
# -*- coding: utf-8 -*-
import math
import os
import time

def menu():
	os.system("clear")
	print ("Menú")
	print ("1) Suma de numeros")
	print ("2) Resta de números")
	print ("3) Multiplicación")
	print ("4) División de números")
	print ("5) Ecuación Cuadrática")
	print ("6) Salir")

def suma():
	sumando1 = int(input("Dame el primer sumando: "))
	sumando2 = int(input("Dame el segundo sumando: "))
	resultado = sumando1 + sumando2
	print (f"La suma de {sumando1} mas {sumando2} es igual a {resultado}")
	time.sleep(2)
	
def resta():
	minuendo = int(input("Dame el minuendo: "))
	sustraendo = int(input("Dame el sustraendo: "))
	diferencia = minuendo - sustraendo
	print (f"La resta de {minuendo} menos {sustraendo} es igual a {diferencia}")
	time.sleep(2)

def mult():
	factor1 = int(input("Dame el factor 1: "))
	factor2 = int(input("Dame el factor 2: "))
	producto = factor1 * factor2
	print (f"{factor1} por {factor2} es igual a {producto}")
	time.sleep(2)

def div():
	dividendo = int(input("Dame el dividendo: "))
	divisor = int(input("Dame el divisor: "))
	cociente = dividendo / divisor
	print (f"{dividendo} ÷ {divisor} es igual a {cociente}")
	time.sleep(2)

def ecuation (a,b,c):
	dis = math.pow (b,2)-4*a*c
	if dis==0:
		print ("Las raices son iguales")
		x1=(-b)/2*a
		x2=x1
		print ("y son: x1=", x1, "x2=", x2)

	elif dis>0:
		print ("Las raices son diferentes")
		x1=(-b+math.sqrt(dis))/2*a
		x2=(-b-math.sqrt(dis))/2*a
		print ("y son: x1=", x1, "x2=", x2)	
	
while True:
	menu()
	op = int(input("Escribe la opción deseada: "))
	if op==1:
		suma()
	elif op==2:
		resta()
	elif op==3:
		mult()
	elif op==4:
		div()
	elif op==5:
		a = int(input("Dame el valor de a: "))
		b = int(input("Dame el valor de b: "))
		c = int(input("Dame el valor de c: "))
		ecuation(a,b,c)
		time.sleep(2)
	elif op==6:
		print ("Ha elegido salir, hasta luego")
		break
		
