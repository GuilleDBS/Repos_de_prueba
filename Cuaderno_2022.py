#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Explorando jupyter")


# Explorando esta IDE para usar con github, probando.

# In[2]:


print("Bloque 2")


# In[3]:


5+4


# probando operación aritmética

# In[4]:


x = 5.1


# In[17]:


#Programa de ejemplo en jupyter notebook
from numpy import *
from matplotlib.pyplot import *

Vector = zeros(70)

for i in range(0,70):   
    Vector[i] = i*0.1

x = Vector
y = sin(x)
z = cos(x)
plot(x,y)
plot(x,z)
grid()


# Probando un codigo for
