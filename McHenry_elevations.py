#!/usr/bin/env python
# coding: utf-8

# In[1]:


import flopy
import pandas as pd
import numpy as np


# In[2]:


top_raw = pd.read_csv(r'C:\Users\Annie\Desktop\UIUC\Spring 2022\Hydro w python\top_elevation.csv')
bottoms_raw = pd.read_csv(r'C:\Users\Annie\Desktop\UIUC\Spring 2022\Hydro w python\bottom_elevations.csv')


# In[73]:


# define necessary parameters
nlay = 10
nrow = top_raw['row'].max()
ncol = top_raw['column'].max()


# In[64]:


# create 2D array of floats for top elevations with shape (nrow,ncol)

# create empty arrays with proper shape that will be populated with elevation data
top_elevation = np.zeros(shape=(top_raw['row'].max(),top_raw['column'].max()))
bottom_elevations = np.zeros(shape=(nlay,bottoms_raw['row'].max(),bottoms_raw['column'].max()))

# loop through raw data to populate empty arrays with elevation data
# top
for i in range(len(top_raw['FID'])):
    top_elevation[int(top_raw.iloc[[i]]['row'])-1][int(top_raw.iloc[[i]]['column'])-1] = float(top_raw.iloc[[i]]['top'])


# In[67]:


# looping through elevation data to populate bottom layer arrays
for layer in range(nlay):
    for i in range(len(bottoms_raw['FID'])):
        bottom_elevations[layer][int(bottoms_raw.iloc[[i]]['row'])-1][int(bottoms_raw.iloc[[i]]['column'])-1] = float(bottoms_raw.iloc[[i]]['Bottom'+str(layer+1)])


# In[69]:


print(top_elevation)
bottom_elevations


# In[71]:


# change units to meters from feet
top_elevation_m = 0.3048*top_elevation
bottom_elevations_m = 0.3048*bottom_elevations


# In[74]:


# create model object
modelname = "my_pumping_model"
m = flopy.modflow.Modflow(modelname, exe_name = 'mf2005')

# create flopy discretization object, length and time are meters (2) and days (4)
dis = flopy.modflow.ModflowDis(model=m, nlay=nlay, nrow=nrow, ncol=ncol, top=top_elevation_m, botm=bottom_elevations_m, 
                               itmuni = 4, lenuni = 2)


# In[ ]:




