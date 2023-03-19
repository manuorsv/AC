#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Puesto que con recursión normal alcanzamos en límite que permite python, lo resolveremos con programación dinámica
#usando una lista.
def es_posible_ganar_con_n_piedras(n):
    lista = []
    #La inicializamos
    for i in range(n+1):
        lista.append(False) 
    #Suponemos que la posición i-ésima de la lista indica si el jugador al que le toca cuando quedan i piedras gana o no.
    #Obviamente, si quedan 0 piedras se gana porque es el otro jugador el que quitó la última.
    lista[0] = True
    #Si queda una piedra el jugador pierde porque no le queda otra opción que quitar la última
    lista[1] = False
    for i in range(2,n+1):
        quita_1 = lista[i-1]
        quita_2 = lista[i-2]
        if i >= 6:
            quita_6 = lista[i-6]
            #Hacemos not de cada opción puesto que esos resultados se refieren a los del otro jugador, puesto que se refieren
            #al siguiente turno. Obviamente que un jugador gane en un turno implica que el otro pierde en ese mismo turno.
            lista[i] = (not quita_1) or (not quita_2) or (not quita_6)
        else:
            lista[i] = (not quita_1) or (not quita_2)
    if lista[n]:
        print("Es posible ganar con " + str(n) + " piedras.")
    else:
        print("No es posible ganar con " + str(n) + " piedras.")
        
es_posible_ganar_con_n_piedras(10**6)

