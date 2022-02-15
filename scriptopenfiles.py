# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 21:39:59 2022

@author: JGabriel
"""
file=open("C:/Users/JGabriel/Downloads/devices.txt")
for a in file:
    a=a.strip("\n")
    print(a)
file.close()

    