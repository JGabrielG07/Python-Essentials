# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:55:43 2022

@author: JGabriel
"""

file=open("C:/Users/JGabriel/Downloads/devices1.txt",mode='a',encoding=(None))
a=input("Desee agregar un nuevo distositivo")
while True a in file:
    a=a.strip("\n")
    print(a)
file.close()


"""
for a in file:
    a=a.strip("\n")
   # print(a)
file.close()


"""