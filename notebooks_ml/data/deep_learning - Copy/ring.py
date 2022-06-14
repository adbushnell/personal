# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:14:02 2020

@author: Albert Tran
"""


# %% -------------------------------------------------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd


# %% -------------------------------------------------------------------------------------------------------------------
# Data creation
#-----------------------------------------------------------------------------------------------------------------------
def get_data(N=50, noise1=2, noise2=2):
    z = 10 # Radius of the circle
    noise1 = 1.5
    noise2 = 2
    
    # Middle: Generate data
    x0 = np.random.normal(0, noise2, size=N)
    y0 = np.random.normal(0, noise2, size=N)
    
    # Ring: Generate points in a circle
    x1 = np.random.uniform(-z, z, size=N)
    y1 = np.sqrt(np.abs(z**2 - x1**2))* np.random.choice([-1,1], size=N)
    
    # Ring: Add noise
    x1 = x1 + np.random.normal(0, noise1, N)
    y1 = y1 + np.random.normal(0, noise1, N)
    
    # Combine data
    x = np.concatenate([x0,x1], axis=0)
    y = np.concatenate([y0,y1], axis=0)
    z = [0]*N + [1]*N
    
    df = pd.DataFrame({'x1':x, 'x2':y, 'y':z})
    return df
