#! /usr/bin/python
# -*- coding: utf-8 -*-

import random

print ("Bienvenido")
print ("##############################################################################")

intentos = 0
generado = random.randint (1,20)

while intentos<5:
    intentos = intentos + 1
    num = int(input ("Que número estoy pensando? "))
    
    if num == generado:
        print ("Eres un drote, adivinaste en"), intentos,("intentos")  
    if num>generado:
        print ("el numero que pensé es menor")
    if num<generado:
        print ("el numero que pensé es mayor")
        
if intentos <6:
    print ("Se acabaron tus intentos, mi numero era"), generado

# No se como omitir el "el numero que pensé es <> o =" en el 5to intento