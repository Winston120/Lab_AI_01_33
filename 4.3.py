# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:58:37 2019

@author: Vitaliy
"""
import random
i=int(input())
g=0
L=0
M=0
while g<i:
    g=g+1
    print("Vash Hid")
    print("1 - Kamin")
    print("2 - Noguci")
    print("3 - papir")
    h=int(input())
    k = random.randint(1,3)
    print(k)
    if h==1 and k==2:
        L=L+1
    elif h==1 and k==3:
        M=M+1
    elif h==2 and k==1:
        M=M+1
    elif h==2 and k==3:
        L=L+1
    elif h==3 and k==1:
        L=L+1
    elif h==3 and k==2:
        M=M+1
    elif h==k:
        g=g-1
        print("Nichya")
        print("Peregraemo")
print("Peremogu PC",M)
print("Peremogu Lydunu",L)
