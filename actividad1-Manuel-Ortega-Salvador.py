#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Devuelve el dígito en posicion n-esima
def digito_pos_n(n):
    if(n < 10):
        return n
    else:
        #Inicializamos la última posición para los enteros de dos cifras
        aux_pos = 9
        #Inicializamos el último número entero de una cifra
        aux_num = 9
        cifras = 1
        while(aux_pos < n):
            cifras += 1
            #Calcula el siguiente nivel (última posición ocupada por los enteros con tantas cifras)
            next_aux = aux_pos + 9 * 10**(cifras-1) * cifras
            #Igual con el último número de tantas cifras del siguiente nivel
            next_aux_num = aux_num * 10 + 9
            if(n <= next_aux):
                break
            else:
                aux_num = next_aux_num
                aux_pos = next_aux
        #Estamos calculando una especie de offset a partir de la última posición ocupada del nivel anterior
        n_aux = n-aux_pos-1
        pos_cifra = n_aux % cifras
        pos_relativo_num = n_aux // cifras
        num = pos_relativo_num + aux_num + 1
        div = num
        for i in range(cifras-pos_cifra):
            if(div<10):
                cifra = div
            else:
                cifra = div % 10
            div = div // 10
        return cifra      
    
#Calculamos el resultado
d1 = digito_pos_n(1)
d10 = digito_pos_n(10)
d100 = digito_pos_n(100)
d1000 = digito_pos_n(1000)
d10000 = digito_pos_n(10000)
d100000 = digito_pos_n(100000)
d1000000 = digito_pos_n(1000000)
sol = d1*d10*d100*d1000*d10000*d100000*d1000000
print(sol)

