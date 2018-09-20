def materialSensitivity(materialList,serieSet,parallelSet,Ri,Ro,T_inside,T_outside):
    from wallCalculation import *
    sensitivityResults = {}
    for gianluca in materials:
        conductivity = gianluca["k"]
        name = gianluca["name"]
        R4={"name":"R4","type":"cond","length":0.16,"area":0.22,"k":conductivity}
        parallelSet = [R3,R4,R5] 
        HeatTransfer = wallHeatTransfer(serieSet,parallelSet,Ri,Ro,T_inside,T_outside)
        sensitivityResults[name] = HeatTransfer
    return sensitivityResults

def multipleMaterialSensitivity(materialList,sizeList,serieSet,parallelSet,Ri,Ro,T_inside,T_outside):
    from wallCalculation import *
    sensitivityMultipleResults = {}
    for gianluca in materials:
        for size in sizeList: 
            conductivity = gianluca["k"]
            name = gianluca["name"]
            R4={"name":"R4","type":"cond","length":size,"area":0.22,"k":conductivity}
            parallelSet = [R3,R4,R5]
            HeatTransfer = wallHeatTransfer(serieSet,parallelSet,Ri,Ro,T_inside,T_outside)
            inputTuple = (name,size)
             #here you should update the dictionary and add a pair including the input string and the value of heat transfer
    return sensitivityMultipleResults
        
 #sensitivityMultipleResults = {"material = glass, size =0.3": 2.786, "material =brick, size =0.45":2.981}

        
glassProp = {"name":"glass", "k": 0.89,"epsilon":0.7}
cementProp = {"name":"cement", "k":1.4, "L=0.3":4500,"L=0.2":2600}
brickProp = {"name":"brick", "k":0.86}
materials = [glassProp,cementProp,brickProp]

conductivity = materials[1]["k"]
name = materials[1]["name"]
T_inside = 20
T_outside = -10
Ri={"name":"Ri","type":"conv","area":0.25,"hConv":10}
R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
R2={"name":"R2","type":"cond","length":0.02,"area":0.25,"k":0.22}
R3={"name":"R3","type":"cond","length":0.16,"area":0.015,"k":0.22}
R4={"name":"R4","type":"cond","length":0.16,"area":0.22,"k":2}
R5={"name":"R5","type":"cond","length":0.16,"area":0.015,"k":0.22}
R6={"name":"R6","type":"cond","length":0.02,"area":0.25,"k":0.22}
Ro={"name":"Ro","type":"conv","area":0.25,"hConv":25}
parallelSet = [R3,R4,R5]
serieSet= [R1,R2,R6]
materials = [glassProp,cementProp,brickProp]

listOfSize = [0.3,0.2,0.45]


ourResult = materialSensitivity(materials,serieSet,parallelSet,Ri,Ro,T_inside,T_outside)
ourResult2 = multipleMaterialSensitivity(materials,listOfSize,serieSet,parallelSet,Ri,Ro,T_inside,T_outside)










from wallCalculation import *
sensitivityResults = {}
for gianluca in materials:
    conductivity = gianluca["k"]
    name = gianluca["name"]
    R4={"name":"R4","type":"cond","length":0.16,"area":0.22,"k":conductivity}
    parallelSet = [R3,R4,R5]
    print parallelSet
    HeatTransfer = wallHeatTransfer(serieSet,parallelSet,Ri,Ro,T_inside,T_outside)
    sensitivityResults[name] = HeatTransfer
    print "SensitivityResults is now: " 
    print sensitivityResults


    
    
    

    




