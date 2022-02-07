# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 19:30:50 2022

@author: JGabriel
"""

#Crear un Scrip que recoja informacion Personal 
nombre=input("Ingrese su Nombre:")
apellido=input("Ingrese su apellido")
locacion=input("Ingrese su ciudad")
edad=int(input("Ingrese su edad"))
if edad>=1 and edad<=10:
   print("la edad es de un nino")
elif edad>=11 and edad<=30:
    print("la edad es de un joven")
else:
    print("El dato ingresado no es un acl")
    





space=" "
print("hola!",nombre,apellido,"su direccion es", locacion, "y su edad es", edad)

