# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:28:50 2022

@author: JGabriel
"""

def l100kmtompg(liters):
    millausa,galonusa=3.785411784,1609.344
    kpg=(millausa/galonusa*1000)
    return 100/liters*kpg

def mpgtol100km(miles):
    x=(235.21/miles)
    return x
    

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.0))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))