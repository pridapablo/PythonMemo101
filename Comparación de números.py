#! /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6
# -*- coding: utf-8 -*-

def mayor3(n1,n2,n3): #<-- defino una función y entre (parentesis) van las variables que usa
    if n1>n2 and n1>n3:
        print (n1, "es el mas grande")
    elif n2>n1 and n2>n3:
        print (n2, "es el mas grande")
    elif n3>n1 and n3>n2:
        print (n3, "es el mas grande")
    elif n1==n2 and n1>n3:
        print (n1, "y", n2, "son mas grandes que", n3)
    elif n1==n3 and n1>n2:
        print (n1, "y", n3, "son mas grandes que", n2)
    elif n2==n3 and n2>n1:
        print (n2, "y", n3, "son mas grandes que", n1)
    else:
        print ("los tres numeros son iguales")

volver="s"

while volver not in ("n", "N", "no", "No", "NO"):

	a=int(input("Dame un numero "))
	b=int(input("Dame otro numero "))
	c=int(input("Dame un tercer numero "))

	mayor3(a,b,c)
	
	volver=(input("¿Quieres volver a empezar? "))