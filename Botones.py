#! /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6
# -*- coding: utf-8 -*-

import tkinter

def function():
	print ("Execlente")
	
root = tkinter.Tk()
button = tkinter.Button (root, text="Que te parece la guía?", command = function)
button.pack()
root.mainloop()