
def compositeWallParallel(resistanceList):
    """This function calculates the resistance value of resstances in parallel
    the input ("resistanceList" is a list of resistances each of which is adictionary
    for example:R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
    and a set of resistances resistanceList= [R1,R2,R3]
    pay attention that the units are as follows: area : m2, length : m, k= W/m.K
    the output resistancesResults is a dictionary with the following structure
     {'R1': 4.62,  'R2': 0.36,'R6': 0.36,'R_total': 5.34}
    the unit of output values is degC/W 
    """
    resistancesResults = {}
    R_tot_inv=0
    for resistance in resistanceList:
        A = resistance["area"]
        L = resistance["length"]
        k = resistance["k"]
        R= round(L/(k*A),2) #I am just taking the first two decimal points
        R_inv= 1/(R)          
        R_tot_inv += R_inv #I am updating the R_tot_inv value
        nameOfResistance = resistance["name"]
        resistancesResults[nameOfResistance] = round(R,2) #here I am saving the R value of each resitance in the results dictionary
    R_tot = 1/R_tot_inv
    resistancesResults["R_total"] = round(R_tot,2)  
    return resistancesResults  
    
def compositeWallSeries(resistanceList):
    """This function calculates the resistance value of resstances in series
    the input ("resistanceList" is a list of resistances each of which is adictionary
    for example:R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
    and a set of resistances resistanceList= [R1,R2,R3]
    pay attention that the units are as follows: area : m2, length : m, k= W/m.K
    the output resistancesResults is a dictionary with the following structure
     {'R1': 4.62,  'R2': 0.36,'R6': 0.36,'R_total': 5.34}
    the unit of output values is degC/W 
    """
    resistancesResults = {}
    R_tot=0
    for resistance in resistanceList:
        A = resistance["area"]
        L = resistance["length"]
        k = resistance["k"]
        R= round(L/(k*A),2)       
        R_tot += R
        nameOfResistance = resistance["name"]
        resistancesResults[nameOfResistance] = round(R,2)
    resistancesResults["R_total"] = round(R_tot,2)  
    return resistancesResults  

def compositeWall(resistanceListSeries,resistanceListParallel):
    """This function calculates the resistance value of resitances in parallel and in series
    Here is the order (resistanceListSeries,resistanceListParallel)
    the input ("resistanceListSeries" is a list of resistances each of which is adictionary
    for example:R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
    and a set of resistances resistanceList= [R1,R2,R3]
    pay attention that the units are as follows: area : m2, length : m, k= W/m.K
    the output resistancesResults is a dictionary with the following structure
     {'R1': 4.62,  'R2': 0.36,'R6': 0.36,'R_total': 5.34}
    the unit of output values is degC/W 
    """
    ResultsWall = {}
    seriesResults=compositeWallSeries(resistanceListSeries)
    R_tot_series = seriesResults["R_total"]
    parallelResults=compositeWallParallel(resistanceListParallel)
    R_tot_parallel = parallelResults["R_total"]
    RtotalWall = R_tot_series + R_tot_parallel
    ResultsWall["Results of series resistances"]=seriesResults
    ResultsWall["Results of parallel resistances"]=parallelResults
    ResultsWall["OverallResistance"] =  RtotalWall
    return ResultsWall
   
def wallConvection(resistance_conv):
    """This function calculates the resistance value of a convective resi
    the input ("resistance_conv" is a dictionary
    for example:Ri={"name":"Ri","type":"conv","area":0.25,"hConv":10}
    pay attention that the units are as follows: area : m2 h= W/m2.K
    the output resistancesResults is a dictionary with the following structure
     {Ri': 5.34}
    the unit of output values is degC/W 
    """    
    resistancesResults={}
    A = resistance_conv["area"]
    h = resistance_conv["hConv"]
    R=round(1/(h*A),2)
    nameOfResistance = resistance_conv["name"]
    resistancesResults[nameOfResistance] = round(R,4)
    resistancesResults["RConv"]=round(R,4)
    return resistancesResults
    
def wallResistance(resistanceListSeries,resistanceListParallel,resistanceConv_internal,resistanceConv_external):
    Result_Wall={}
    compositeWallResults = compositeWall(resistanceListSeries,resistanceListParallel)
    R_compositeWall = compositeWallResults["OverallResistance"]
    
    internalConvectionResult = wallConvection(resistanceConv_internal)
    R_internal_convection = internalConvectionResult["RConv"]
    
    externalConvectionResult = wallConvection(resistanceConv_external)
    R_external_convection = externalConvectionResult["RConv"]
    
    R_overall_wall = R_compositeWall+R_internal_convection+R_external_convection
    Result_Wall["OverallWallResistance"] = R_overall_wall
    Result_Wall["detailsOfCompositeWall"] = compositeWallResults
    Result_Wall["detailsOfInternalConvection"] = internalConvectionResult
    Result_Wall["detailsOfExternalConvection"] = externalConvectionResult
    return Result_Wall
    
Ri={"name":"Ri","type":"conv","area":0.25,"hConv":10}
R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
R2={"name":"R2","type":"cond","length":0.02,"area":0.25,"k":0.22}
R3={"name":"R3","type":"cond","length":0.16,"area":0.015,"k":0.22}
R4={"name":"R4","type":"cond","length":0.16,"area":0.22,"k":0.72}
R5={"name":"R5","type":"cond","length":0.16,"area":0.015,"k":0.22}
R6={"name":"R6","type":"cond","length":0.02,"area":0.25,"k":0.22}
Ro={"name":"Ro","type":"conv","area":0.25,"hConv":25}

parallelSet = [R3,R4,R5]
resultsParallel=compositeWallParallel(parallelSet) 
serieSet= [R1,R2,R6]
resultsSeries=compositeWallSeries(serieSet)
results = compositeWall(serieSet,parallelSet)

FinalWallResults = wallResistance(serieSet,parallelSet,Ri,Ro)

def wallHeatTransfer(resistanceListSeries,resistanceListParallel,resistanceConv_internal,resistanceConv_external, T_inside,T_outside):
    R_wall_results = wallResistance(resistanceListSeries,resistanceListParallel,resistanceConv_internal,resistanceConv_external)
    R_wall = R_wall_results["OverallWallResistance"]
    Q=(T_inside-T_outside)/R_wall
    Q_formatted = round(Q,4)
    return Q_formatted
    
Ti =20
To= -10
HeatTrasfer = wallHeatTransfer(serieSet,parallelSet,Ri,Ro,Ti,To)