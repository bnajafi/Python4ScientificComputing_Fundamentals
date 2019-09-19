
# create dictionary with different values of k for the brick object
#input dictionary  
glassProp = {"name":"glass", "k":0.9}
brickProp ={"name":"brick", "k": 0.87}
cement ={"name":"cement", "k": 1.5}
material_list = [ glassProp,brickProp,cement]

def materialSensitivity(material_List, .....)
    #for material in material_List
    # you need to import wallHeatTransfer from wallCalculation Script
    heatTransfer = wallHeatTransfer(resistanceListSeries,resistanceListParallel,resistanceConv_internal,resistanceConv_external, T_inside,T_outside)
    
    
#out put should be like this: result_sensitivity=  {"glass":253,"brick": 350,... } 
# the ouput can also be a list of dictionaries [{"name":"glass","HeatTransfer" : 253},{"name":"brick","HeatTransfer" : 352}]   