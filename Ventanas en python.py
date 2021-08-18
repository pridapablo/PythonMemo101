#! /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6
# -*- coding: utf-8 -*-

import tkinter as tk #<- Si *T*kinter está en mayúscula: estoy en python 2.7

ventana = tk.Tk() #<- renombro tk a ventana
ventana.title("Hola todos")
ventana.geometry("600x1000")
ventana.configure(background="pink")

etiqueta1=tk.Label(ventana,text="Ya me voy") #<- DEFINO mi ventana
etiqueta1.pack() #<- Mando LLAMAR mi ventana (lo empaqueto [pack])

entrada=tk.Entry(ventana)
entrada.pack()


ventana.mainloop()