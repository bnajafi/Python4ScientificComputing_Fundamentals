# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 07:31:52 2018

@author: behzad
"""

import os
import sys
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()


import os 
os.chdir(r"C:\Users\behzad\Dropbox\2 Teaching Activities\0 EETBS 2018\forked_repos\Python4ScientificComputing_Fundamentals\A 2018-2019")
import wallFunctions

from wallFunctions import ThermalResDict
print(ThermalResDict)