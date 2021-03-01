# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:26:36 2020

@author: 427208
"""

import pandas as pd
import numpy as np


file_new = r"C:/automation/output.xlsx"
file_old = r"C:/automation/output_2.xlsx"

df_new = pd.read_excel(file_new)
df_old = pd.read_excel( file_old)


if len(df_new) != len(df_old):
    print("Both new and old files have different rows")
else:
    print("Both files are same rows")
status = []

for index, (i,j) in enumerate( zip( df_new[0], df_old[0] ) ):
    #print(i,j)
    
    if i !=  j:
        #print(i, j)
        status.append("modified")
    else:
        status.append("no_change")
        
        
df_new['status'] = status
df_new.to_excel("final_output.xlsx")

