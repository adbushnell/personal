# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:57:10 2020

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
def get_data(N=50, marker=5, std_line=1, std_cloud=1):
    '''
    Creates that that looks like a percent sign.
    Data points on the line are class 0, and the circles are class 1.
    '''
    x_line = np.linspace(-(marker + 3*std_cloud), marker + 3*std_cloud, N)
    y_line = x_line + np.random.normal(0, std_line, N)
    
    x_cloud1 = np.random.normal(marker, std_cloud, N)
    y_cloud1 = np.random.normal(-marker, std_cloud, N)
    
    x_cloud2 = np.random.normal(-marker, std_cloud, N)
    y_cloud2 = np.random.normal(marker, std_cloud, N)
    
    df_line   = pd.DataFrame({'x1':x_line,   'x2':y_line,   'y':[0]*N})
    df_cloud1 = pd.DataFrame({'x1':x_cloud1, 'x2':y_cloud1, 'y':[1]*N})
    df_cloud2 = pd.DataFrame({'x1':x_cloud2, 'x2':y_cloud2, 'y':[1]*N})
    
    df = pd.concat([df_line, df_cloud1, df_cloud2], axis=0)
    return df


