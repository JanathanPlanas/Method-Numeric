#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import numpy for array processing
import numpy as np
import math


# In[5]:


def soluciona_com_pivotamento_parcial(M, b, verbose=False):
    print(20*'-', '\n', 'Pivotamento parcial', '\n', 20*'-')
    # quantidade de linhas e colunas da matriz quadrada M 
    n = len(M)

    if b.size != n:
        raise ValueError(f"Inválido: b deve ser n x 1 e M deve ser n x n. Recebido: b {b.size}x1 e M {n}x{n}")

    # percorreremos a k-ésima linha de pivot.
    for k in range(n-1):
        # escolha do maior pivot
        maximo = abs(M[k:, k]).argmax() + k

        if M[maximo, k] ==0:
            raise ValueError('Impossível solucionar, pois a Matriz é singular.')
        
        # troca de linhas
        if maximo != k:
            # troca k-ésima linha pela linha de índice = "maximo"
            M[[k, maximo]] = M[[maximo ,k]]
            b[[k, maximo]] = b[[maximo, k]]

        for lin in range(k+1, n):
            # multiplicador da matriz para atualização L_i = L_i + m_ij* L_j
            m = M[lin][k]/M[k][k]

            # a unica nesta coluna ja que o resto é zero
            M[lin][k] = m

            for col in range(k+1, n):
                M[lin][col] = M[lin][col] - m * M[k][col]
            
            #coluna de solução
            b[lin] -= m*b[k]

    if verbose == True:
        print(f' M: {M} \n b: {b} \n')

    # hora de substituir e achar a solução x
    x = np.zeros(n)
    k = n-1
    x[k] = b[k]/M[k, k]
    
    while k >=0:
        x[k] = (b[k] - np.dot(M[k, k+1:], x[k+1:]))/M[k,k]
        k -=1
    
    if verbose == True:
        for i in range(n):
            print('\n {} \n x{} = {} \n {}'.format(10*'=', i+1, x[i], 10*'='))
        print(' \n {} \n x = {} \n {}'.format(20*'=', x, 20*'='))
    return x


# In[4]:


A = np.random.randint(0,99,(3,3))
B = np.random.randint(0,99,3)
x = gauss_elimination(A,B)
for i in range(len(B)):
    print("x"+str(i)+" = "+str(x[i]))
print("Matriz A:", A)
print("\n")
print("Matriz B:", B)

# In[ ]:




