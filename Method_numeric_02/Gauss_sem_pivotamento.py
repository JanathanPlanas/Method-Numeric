#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import numpy for array processing
import numpy as np
import math


# In[3]:


def soluciona_sem_pivotamento(M, b, verbose=False):
    """ 
    M : matriz nxn formada pelos coeficientes do sistema de equações
    b : vetor nx1 de valores associados a cada equação
    """
    print(20*'-', '\n', 'Sem pivotamento', '\n', 20*'-')
    # tamanho das linhas e colunas da matriz quadrada M
    n = len(M)
    if b.size != n:
        raise ValueError(f"Inválido: b deve ser n x 1 e M deve ser n x n. Recebido: b {b.size}x1 e M {n}x{n}")

    for linha_pivot in range(n-1):
        for linha in range(linha_pivot+1, n):
            # coeficiente m = razao entre primeiros valores das linhas escolhidas
            m = M[linha][linha_pivot]/M[linha_pivot][linha_pivot]

            # rodando as colunas
            for col in range(linha_pivot+1, n):
                M[linha][col] = M[linha][col] - m*M[linha_pivot][col]
            # coluna de solução da equação
            b[linha] = b[linha] - m*b[linha_pivot]

    if verbose == True:
        print(f'M : {M} \n b: {b}')

    x = np.zeros(n)
    k=n-1
    x[k] = b[k]/M[k, k]
    while k >= 0:
        x[k] = (b[k] - np.dot(M[k, k+1:], x[k+1:]))/M[k,k]
        k-=1
    if verbose == True:
        for i in range(n):
            print('\n {} \n x{} = {} \n {}'.format(10*'=', i+1, x[i], 10*'='))
        print(' \n {} \n x = {} \n {}'.format(20*'=', x, 20*'='))
    return x


# In[4]:


A = np.array([[2,4,8],[-2,-8,2],[8,-4,-2]])
B = np.array([2,-20,2])


# In[ ]:




