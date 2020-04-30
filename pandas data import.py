# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:31:15 2020

@author: Marcus
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('flightdata.txt', delim_whitespace=True)

print(df.columns)

x = (df['<Clock>[ms]'])
y = (df['<Height>[m]'])

print(x,y)


# <Clock>[ms] x-axis
# <Height>[m] y-axis


