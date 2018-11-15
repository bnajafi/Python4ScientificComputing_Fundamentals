# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 06:31:28 2018

@author: behzad
"""
import pandas as pd
#First methodology 
import os
Folder_WhereIwas= os.getcwd()
Folder_whereThoseTablesAre = r"C:\Users\behzad\Dropbox\2 Teaching Activities\0 EETBS 2018\forked_repos\Python4ScientificComputing_Fundamentals\A 2018-2019\Tables"
os.chdir(Folder_whereThoseTablesAre)
window_DF = pd.read_csv("windows.csv", sep=";", index_col = 0, header=0) 
os.chdir(Folder_WhereIwas)

# Second way of handling this location problem
name_file_windows = "windows.csv"
path_file_windows = os.path.join(Folder_whereThoseTablesAre,name_file_windows) 
window_DF = pd.read_csv(path_file_windows, sep=";", index_col = 0, header=0) 
window_DF.head(4)
window_DF.tail(1)
window_DF.index
window_DF.columns
window_DF.loc["west",'Window_ID']
window_DF.loc[:,'width']
window_DF['width']
window_DF['Area']=window_DF['width']*window_DF['Height']
window_DF.to_csv(path_file_windows,sep=";") # I am adding this sep=";" just because if not I will have to rearrange it in excel and I am lazy !

name_file_modifiedWindows="window_modified.csv"
path_file_modifiedwindows = os.path.join(Folder_whereThoseTablesAre,name_file_modifiedWindows) 
window_DF.to_csv(path_file_modifiedwindows,sep=";") # I am adding this sep=";" just because if not I will have to rearrange it in excel and I am lazy !




