# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:51:33 2019

@author: Vitaliy
"""
a = float(input())
b = float(input())
c = float(input())
if a+b>c and a+c>b and b+c>a:
    print("YES")
else: 
    print("NO")
