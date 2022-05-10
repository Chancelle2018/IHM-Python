# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 12:24:32 2021

@author: chane
"""



s=0.05
x1=0.0

def x(n):
    if n>0:
        return x1+(n-1)*s
    else:
        return x1+(n+1)*s


def fonction(n):
    return x(n)**2-1.5*x(n)

def pas_f():
    n=1
    if fonction(2)<fonction(1) :
        while fonction(n+1)<fonction(n): 
            n+=1
        a=x(n-1)
        b=x(n)
    elif fonction(2)>fonction(1):
        while fonction(n+1)>fonction(n):
            n-=1
        a=x(n-1)
        b=x(n)
    elif fonction(2)==fonction(3):
        a=x(1)
        b=x(2)
    elif fonction(2)>fonction(1) and fonction(2)>fonction(1):
        a=x(-2)
        b=x(2)
    return n,a,b

resultat=pas_f()
n=resultat[0]
a=resultat[1]
b=resultat[2]   
print("Le point minimum x* est entre ",a," et ",b,". f(x*)=",fonction(n))
                 
             

    