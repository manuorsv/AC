#!/usr/bin/env python
# coding: utf-8

# In[6]:


from math import sqrt, gcd

def es_primo(n):
    if n < 2:
        return False
    
    elif n == 2:
        return True
    else:
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n%i == 0:
                return False
        return True
    
def numeros_Carmichael():
    cont = 0
    N = 1
    while cont < 10:
        pseudoprimo = True
        if not (N<=2 or es_primo(N)):
            for a in range(N):
                if gcd(a,N) == 1 and pow(a,N-1,N) != 1:
                    #Ya sabemos que no es pseudoprimo y podemos dejar de comprobar
                    pseudoprimo = False
                    break
            if pseudoprimo:
                print(N)
                cont += 1
        N += 1
        
numeros_Carmichael()

