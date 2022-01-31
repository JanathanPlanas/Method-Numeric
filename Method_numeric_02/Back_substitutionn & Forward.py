#!/usr/bin/env python
# coding: utf-8

# In[1]:


# BACK back_substitution
import math 
import numpy as np
import sys
def back_substitution(A: np.ndarray, b: np.ndarray):
  n = len(A) #  A copy from the length of answer array A
  x = np.zeros(b.size) # Creating eh copy length of array b due their length would be at the same of X 
      #VALIDATION CODING
  if len(b) != len(A): #This condition check if we working at the same side of Matrix
      raise ValueError("Invalid situation , both matrix should be the type Ax=B")
      exit
      None
      #VALIDATION CODING
  for i in list(range(1,n+1,1)) :# This looping create the response vector X based on input values from back_substitution(A,B)
      if(math.fabs(A[i-1][i-1]) == 0.0):
          raise ValueError("ERROR, Incorrect input data ")
          exit
          None
      #VALIDATION CODING
      if(math.fabs(b[i-1]) == 0.0):
          raise ValueError("ERROR, Incorrect input data ")
          exit
          None
      # back_substitution METHOD  
  x[n-1] = b[n-1]/A[n-1][n-1] # Looking for X3 
  c = np.zeros((n,n)) # Numerator 
  for i in range(n-2, -1, -1):
      bb = 0 #The summation variable 
      for j in range (i+1, n): # This looping is The Summation of J until N
          bb += A[i, j]*x[j]

      c[i][i] = b[i] - bb
      x[i] = c[i][i]/A[i][i]
  return x


# In[4]:


A = np.array([[2, 4, 8], [0, -4, 10], [0, 0, -84]]) # Input values of an upper triangular matri
B = np.array([[2],[-18],[84]])
x = back_substitution(A,B)
#Printing each value from vector X 
for i in range(len(B)):
    print("x"+str(i)+" = "+str(x[i]))


# In[5]:


def forward_substitution(A: np.ndarray, b: np.ndarray):
    n = len(A) #  A copy from the length of answer array A
    x = np.zeros(b.size) # Creating eh copy length of array b due their length would be at the same of X 
        #VALIDATION CODING
    if len(b) != len(A): #This condition check if we working at the same side of Matrix
        raise ValueError("Invalid situation , both matrix should be the type Ax=B")
        exit
        None
        #VALIDATION CODING
    for i in list(range(1,n+1,1)) :# This looping create the response vector X based on input values from back_substitution(A,B)
        if(math.fabs(A[i-1][i-1]) == 0.0):
            raise ValueError("ERROR, Incorrect input data ")
            exit
            None
        #VALIDATION CODING
        if(math.fabs(b[i-1]) == 0.0):
            raise ValueError("ERROR, Incorrect input data ")
            exit
            None
        # forward_substitution METHOD  
    x[0] = b[0]/A[0][0] # Looking for X1
    c = np.zeros((n,n)) # Numerator 
    for i in range(c.shape[0]):
        bb = 0 #The summation variable 
        for j in range (i): # This looping is The Summation of J until N
            bb += A[i][j]*x[j]

        c[i][i] = b[i] - bb
        x[i] = c[i][i]/A[i][i]
    return x


# In[6]:


A = np.array([[4, 0, 0], [5, 2, 0], [3, 1,6]]) # Input values of an lower triangular matriz
B = np.array([[2],[-3],[20]])
x = forward_substitution(A,B)
#Printing each value from vector X 
for i in range(len(B)):
    print("x"+str(i)+" = "+str(x[i]))


# In[ ]:




