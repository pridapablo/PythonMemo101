#! /usr/bin/python
# -*- coding: utf-8 -*-

def Divisores (n,volver):
    
    if n<=0:
        print ("Te pedí un número entero mayor a cero ")
        volver="Si"
        # Mi idea con este volver=si es que el programa se reinicie si se introduce un número menor o igual a cero, sin volver a preguntar si quieres o no
    else:
        # No se como hacer que salga así (sin cambiar de linea):
        # Los divisores de (n) son (1), (d) y (n) 
        print (n), "es divisible entre", (1)
        for d in range(2,n):
            if n%d==0:
                print (n), "es divisible entre", (d)
        print (n), "es divisible entre", (n)

volver="s"

while volver not in ("n", "N", "no", "No", "NO"):
    print ("DIVISORES")
    print ("##############################################################################")
    n=int(input("Escribe un numero entero mayor a cero "))
    
    Divisores(n,volver)
    
    volver=(input("¿Quieres probar otro numero? "))
    # Pongo (raw_input) para que el usuario no tenga que poner su respuesta entre comillas
