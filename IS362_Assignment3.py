#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import sys


# In[8]:


print('Python version ' + sys.version)
print('Pandas version: ' + pd.__version__)


# In[42]:


trip = {
    "day": [1, 2, 3, 4],
    "milage": [55, 60, 50, 55],
    "total_miles": [55, 115, 165, 120]
}    


# In[43]:


trip['milage']


# In[44]:


df = pd.DataFrame(trip)


# In[45]:


df


# In[29]:


df['milage']


# In[30]:


type(df['milage'])


# In[91]:


milage = [55, 60, 50, 55]
total=0
for item in milage:
    total+=item
print("Miles:", total)


# In[ ]:




