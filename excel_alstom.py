# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 19:48:12 2020

@author: 427208
"""


import pandas as pd

# change the input file and folder name

file_name = r"Grades 6.6 new input.xlsx"

df = pd.read_excel( file_name , header=None)


output = []

col_1  = "/infrastructure/physicalElements/tracks/track/trackElements/grades/grade" + df[0]

col_2 = "/infrastructure/physicalElements/tracks/track/trackElements/grades/grade/" + df[1]

col_3 = "/infrastructure/physicalElements/tracks/track/trackElements/grades/grade/" + df[2]

col_4 = "/infrastructure/physicalElements/tracks/track/trackElements/grades/grade/" + df[3]

df = pd.concat( [ col_1, col_2, col_3, col_4 ], axis=1 )


for i, row in df.iterrows():
    #print(row)
     for j, column in row.iteritems():
            #print(column)
            output.append(column)
            #print("-------")
            
            
df = pd.DataFrame( output )

df.to_excel("output.xlsx")


