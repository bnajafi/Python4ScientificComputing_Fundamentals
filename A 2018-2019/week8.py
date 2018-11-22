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

latitude  = 45
location_deltaT_cooling = 7.9 
location_deltaT_heating = 24.9 
location_DR_cooling= 11.9

C_Value = location_deltaT_cooling - 0.46*location_DR_cooling
window_DF["C_value"]= C_Value


name_file_IAC_Cl="IAC_cl.csv"
path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0) 
IAC_cl_DF.head(3)
IAC_cl_DF.loc["1c","BlindsDark"]



def IAC_CL_finder(windowID,intShadingID):  
    name_file_IAC_Cl="IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0) 
    IAC_cl_value = IAC_cl_DF.loc[windowID,intShadingID]
    return IAC_cl_value

IAC_CL_finder("1c","BlindsDark")  

def IAC_CL_finder_correct(row):
    windowID = row["Window_ID"]
    intShadingID = row["IntShading_ID"]
    name_file_IAC_Cl="IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0) 
    IAC_cl_value = IAC_cl_DF.loc[windowID,intShadingID]
    return IAC_cl_value


thisWindowRow= window_DF.loc["east",:]

IAC_CL_finder_correct(thisWindowRow)

window_DF["IAC_cl"]=window_DF.apply(IAC_CL_finder_correct,axis=1)

window_DF["IAC"]=  1.0+(window_DF["IAC_cl"]-1.0)*window_DF["IntShading_closeness"]

window_DF.to_csv(path_file_modifiedwindows,sep=";") # I am adding this sep=";" just because if not I will have to rearrange it in excel and I am lazy !

# How can I make a range of numbers!

x1 = range(1,11,2) # (start,stop,step) !it does not inlcude the stop one!

# This is an awesome command if we want to create range of integers !!

# IF I would like to create a range of floats: I should use numpy
# I fyou have not imported it yet
import numpy as np
import pandas as pd
A1 = np.arange(0.1,2,0.1)

# The other vector we might need is the one where we just know the start, the stop and number of points
A2 = np.linspace(0,10,50)

# Now let's use this !

X=np.arange(-10,10.1,0.1)
Y=X**2-5

def myFunc(x):
    y=x**2-5
    return y
X_series = pd.Series(X)
Y_series = X_series.apply(myFunc)




