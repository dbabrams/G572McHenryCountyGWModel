# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 00:56:05 2022

@author: andrewm4
"""

import pandas as pd
import seaborn as sns
from simpledbf import Dbf5
import numpy as np

# read in dbf to pandas dataframe
file = 'C:/users/andrewm4/Documents/Hydro_572/GitHub/G572McHenryCountyGWModel/GISuploads/hydraulic_conductivity.dbf'
dbf = Dbf5(file)
df = dbf.to_dataframe()
df.head()

# create dataframes of the 10 zones, Kx, Ky, and Kz
zone = df[df.columns[pd.Series(df.columns).str.contains("Z")]]
x = df[df.columns[pd.Series(df.columns).str.contains("x")]]
y = df[df.columns[pd.Series(df.columns).str.contains("y")]]
z = df[df.columns[pd.Series(df.columns).str.contains("z")]]

# define the function that converts data frame to array; reshapes it and saves as variable
# 3D array of 10 layers by 205 rows by 225 columns
def array_shaper(j):
    j = j.to_numpy()
    j = np.reshape(j, (205,225,10)) # 205 = y; 225 = x
    return j

# save function output to variables
zone_reshaped = array_shaper(zone)
x_reshaped = array_shaper(x)
y_reshaped = array_shaper(y)
z_reshaped = array_shaper(z)

# check shape
print(zone_reshaped.shape)
print(x_reshaped.shape)
print(y_reshaped.shape)
print(z_reshaped.shape)