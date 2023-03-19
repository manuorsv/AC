#!/usr/bin/env python
# coding: utf-8

# In[4]:


from math import sqrt, gcd, log, ceil
import random

def es_primo(n):
    if n < 2:
        return False
    
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n%i == 0:
                return False
        return True

def pollard_pm1(N,B):
    if es_primo(N):
        return 1,N
    
    #Llenamos la lista de primos hasta B
    primos = []
    for i in range(2, B+1):
        if es_primo(i):
            primos.append(i)
    
    #Calculamos beta
    beta = 1
    for p in primos:
        ent_log = ceil(log(N,p))
        beta *= pow(p,ent_log)
    
    #Hacemos un bucle infinito puesto que encontrará seguro una factorización que hará terminar la función
    while True:
        a = random.randrange(1,N)
        x = gcd(a,N)
        y = gcd(pow(a,int(beta),N)-1,N)
        if x != 1:
            return x,N//x
        elif y != N:
            return y, N//y
        

print(pollard_pm1(1542201487980564464479858919567403438179217763219681634914787749213,100))

