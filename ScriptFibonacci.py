# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:38:44 2022

@author: JGabriel
"""

def fibonaci(n):
    a= 0
    b=1
    while a < n:
        print(a)
        a, b = b, a+b  #c=a+b,a=b b=c
    print()
fibonaci(6)
