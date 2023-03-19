#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Para comprobar si hemos vuelto a la configuracion inicial
def comprueba_solucion(n_cajas, cajas_conf):
    for i in range(n_cajas):
        if cajas_conf[i] != 1:
            return False
    return True;
    
#Funcion para resolver el problema para n cajas    
def problema_cajas(n_cajas):
    cajas = []
    #Inicializamos las cajas con una bola
    for i in range(n_cajas):
        cajas.append(1)
    
    repite_conf = False
    caja_turno = 0
    iteracion = 0
    #Repetimos hasta que la configuracion inicial se repita
    while not repite_conf:
        #Vaciamos la caja
        bolas_caja = cajas[caja_turno]
        cajas[caja_turno] = 0
        #Vamos llenando las siguientes cajas con una bola
        for i in range(bolas_caja):
            caja_turno += 1
            if caja_turno == n_cajas:
                caja_turno = 0
            cajas[caja_turno] += 1
        repite_conf = comprueba_solucion(n_cajas, cajas)
        iteracion += 1
    print(iteracion) 

problema_cajas(100)

