#! /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6
# -*- coding: utf-8 -*-

import os
import tkinter as tk
ventana = tk.Tk()

Suma = tk.Button (ventana, text = "Suma")
Resta = tk.Button (ventana, text = "Resta")
Multiplicacion =tk.Button (ventana, text = "Multiplicación")
Division = tk.Button (ventana, text = "División")
Salir = tk.Button (ventana, text = "Salir")
	
def dibujamenu():	
	Suma.pack()
	Resta.pack()
	Multiplicacion.pack()
	Division.pack()
	Salir.pack()
	

ventana.title("Calculadora")
ventana.geometry("1000x1000")
ventana.configure(background = "light sky blue")

dibujamenu()


	