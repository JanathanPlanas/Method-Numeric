#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
import numpy as np
import sys


# In[121]:


def _poly_newton_coefficient(x: np.ndarray, y: np.ndarray):
    #x: list or np array contanining x data points
    #y: list or np array contanining y data points

    m = len(x)
    x = np.copy(x)
    a = np.copy(y) # This assure the size number from vector are equal to input data y 
    for k in range(1, m): # This looping assure the math calculationf for each interaction
        a[k:m] = (a[k:m] - a[k - 1])/(x[k:m] - x[k - 1]) # The formula from newton interaction

    return a

def newton_polynomial(x_data: np.ndarray, y_data: np.ndarray, x ):
    
    #Validataion CODE
    if x_data.size !=y_data.size: #If the both vector isn't the sami size , the code should stop
        raise ValueError("ERROR, Incorrect input data ")
    
        None
        
        #Validataion CODE
    if x_data.ndim !=y_data.ndim or x_data.ndim > 1 or y_data.ndim > 1  : #If the both vector isn't the sami size of dimension, the code should stop
        raise ValueError("ERROR, Incorrect input data ")
        None
        
        #Validataion CODE
    if x< 0:
        raise ValueError("ERROR, Incorrect input data ")
        None
        
        
    #x_data: data points at x
    #y_data: data points at y
    #x: evaluation point(s)
    
    a = _poly_newton_coefficient(x_data, y_data) # aply the newton method formula
    n = len(x_data) - 1  # Degree of polynomial
    p = a[n]

    for k in range(1, n + 1): # This loop print the output value from newton polynomial
        p = a[n - k] + (x - x_data[n - k])*p
        print("p:"+ str(k)+"=", p)


# In[122]:



x=np.array([ 0.25, 0.75 ,1.25 ,1.5 ,2])
y=np.array([-0.45 ,-0.6 ,0.7 ,1.88 ,6.0])
newton_polynomial(x,y,1.15)
a =_poly_newton_coefficient(x,y)
for i in range (0,x.size,1):
    print("a :"+str(i)+"=",a[i])


# In[ ]:




