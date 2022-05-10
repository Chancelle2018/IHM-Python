# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 12:24:50 2021

@author: chane
"""

#s=0.05
#x1=0.0

def x(n,s,x1):
    if n>0:
        return x1+(n-1)*s
    else:
        return x1+(n+1)*s


def fonction(n,s,x1):
    return x(n,s,x1)**2-1.5*x(n,s,x1)

def pas_a():
    x1=0.0
    s=0.05
    n=1
    if fonction(2,s,x1)<fonction(1,s,x1) :
        while fonction(n+1,s,x1)<fonction(n,s,x1): 
            n+=1
            s=2*s
        a=x(n-1,s,x1)
        b=x(n,s,x1)
    if fonction(2,s,x1)>fonction(1,s,x1):
        while fonction(n+1,s,x1)>fonction(n,s,x1):
            n-=1
            s=2*s
        a=x(n-1,s,x1)
        b=x(n,s,x1)
    elif fonction(2,s,x1)==fonction(3,s,x1):
        a=x(1,s,x1)
        b=x(2,s,x1)
    elif fonction(2,s,x1)>fonction(1,s,x1) and fonction(2,s,x1)>fonction(1,s,x1):
        a=x(-2,s,x1)
        b=x(2,s,x1)
    return n,a,b,s

resultat=pas_a()
n=resultat[0]
a=resultat[1]
b=resultat[2]   
s=resultat[3]
print("Le point minimum x* est entre ",a," et ",b)
