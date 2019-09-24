import math
V=int(input())
h=int(input())
So=3*V/h
a=So**(1/2)
f=(h**2+(a/(2*math.tan(math.pi/4)))**2)**(1/2)
Sb=1/2*a*f*4
print(round(Sb,3))