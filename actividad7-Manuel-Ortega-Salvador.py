#!/usr/bin/env python
# coding: utf-8

# In[34]:


from math import gcd, sqrt
import random
import matplotlib.pyplot as plt
import numpy as np
    
def simbolo_Jacobi(a,N):
    t = 1
    while a != 0:
        while a%2 == 0:
            a //= 2
            r = N%8
            if r == 3 or r == 5:
                t = -t
        a, N = N, a
        if a%4 == 3 and N%4 == 3:
            t = -t
        a %= N
    if N == 1:
        return t
    else:
        return 0

def test_de_solovay_strassen(N,k):
    if N>2 and N%2 == 0:
        return False
    else:        
        for i in range(k):
            a = random.randrange(1,N)
            u = gcd(a,N)
            v = pow(a,(N-1)//2,N)
            #Queremos que sea -1 en caso de que la potencia sea N-1 para que pueda coincidir con el símbolo de Jacobi
            if v == N-1 and N!=2:
                v = -1
            if u != 1: 
                return False
            if v != simbolo_Jacobi(a,N):
                return False;
        return True

def generar_primo(n,k):
    found = False
    cnt = 1
    while not found:
        N = random.randrange(1,10)
        for _ in range(n-1):
            a = random.randrange(10)
            N *= 10
            N += a
        if test_de_solovay_strassen(N,k):
            found = True
            return (N,cnt)
        else:
            cnt += 1
            
def generar_histograma():
    valores = []
    for _ in range(100):
        N,cnt = generar_primo(300,20)
        valores.append(cnt)
    
    plt.xlabel('cnt')
    plt.ylabel('Frecuencia')
    plt.hist(valores,bins=range(min(valores),max(valores)+1,50))
    plt.savefig("histograma.png")

