# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:31:12 2022

@author: JGabriel
"""

def isPrime(x):
    if x<=1:
        return "False"
    elif x==2:
        return "True"
    else:
        for i in range(2,x):
          if x%i==0:
            return "False"
        return "True"
    