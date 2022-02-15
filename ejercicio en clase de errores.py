# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:28:30 2022

@author: JGabriel
"""
try:
    y=1/0
except ArithmeticError:
    print("Error de otro tipo de artimerica")
except ZeroDivisionError:
        print("You cannot divide by zero,sorry.") 
    
    