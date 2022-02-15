# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:13:40 2022

@author: JGabriel
"""
try:
    x=int(input("Enter a number:"))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero,sorry.")
except ValueError:
    print("You must enter a integer value:")
except:
        print("Oh dear,something went wrong")
        print(" end ")
        
        