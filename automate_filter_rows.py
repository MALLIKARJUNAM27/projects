# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 20:41:26 2021

DescriptioN:
    
How to use:
    

@author: 427208
"""

import pandas as pd


def main():

    # input files before run the code 
    
    file = r"C:/automation/Template_count.xlsx"
    #file = r" "
    
    output_file_name = r"counte_temple_without_id_name.xlsx"
    
    # ---------------------------
    
    
    df = pd.read_excel(file)
    
    
    df_id_name_remove = df[ ~df['ElementPathParametersMain ID elementMain NAME element'].str.match(r'ID|NAME')]
    
    print("Created the filetered output as counte_temple_without_id_name.xlsx")
    df_id_name_remove.to_excel(output_file_name)
    
    #get the ref= match
    df_ref = df_id_name_remove[df_id_name_remove["ElementPathParametersMain ID elementMain NAME element"].str.contains("/infrastructure/logicalElements/boundaries/boundary/location/tracksideAbsoluteLocation/measurementUncertainty/value=")]
    
    # print number of rows starts with id
    #df_id = df_id_name_remove[df_id_name_remove["ElementPathParametersMain ID elementMain NAME element"].str.contains("id=")]
    
    print("# of ref=",df_ref.count() )
   
  
if __name__ == "__main__":        
    main()