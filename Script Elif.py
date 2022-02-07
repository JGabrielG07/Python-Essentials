# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 19:20:59 2022

@author: JGabriel
"""

acl=int(input("Ingrese el # de acl"))
if acl>=1 and acl<=99:
    print("la acl es estandar")
elif acl>=100 and acl<=199:
    print("la acl es extendida")
else:
    print("El dato ingresado no es un acl")
    
    