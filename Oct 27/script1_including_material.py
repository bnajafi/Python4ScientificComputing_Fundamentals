"""
MaterialLibrary={"outSideSurfaceWinter":{"RValue":0.03},"outSideSurfaceSummer":{"RValue":0.044},
"insideSurface":{"RValue":0.12},"airSpace-13mm":{"RValue":0.16,"length-mm":13},"airSpace-20mm":{"RValue":0.17,"length-mm":20},
"airSpace-40mm":{"RValue":0.16,"length-mm":40},"airSpace-90mm":{"RValue":0.16,"length-mm":90},
"insulation-glassFiber-25mm":{"RValue":0.7,"length-mm":25},"insulation-mineralFiberBatt-25mm":{"RValue":0.66,"length-mm":25},
"insulation-urethaneRigidFoam-25mm":{"RValue":0.98,"length-mm":25},"stucco-25mm":{"RValue":0.037,"length-mm":25},
}
"""





materialLength=200 #mm
materialLibrary = {"commonBrick-100mm":{"RpValue":0.17,"length":100},
"stucco-25mm":{"RpValue":0.037,"length":25}}
AvailableMaterialIDs= materialLibrary.keys()
ID="commonBrick-100mm"
originalMaterialLength = materialLibrary[ID]["length"]
originalMaterialRValue=materialLibrary[ID]["RpValue"]
R_p=originalMaterialRValue*materialLength/originalMaterialLength

R1={"name":"R1","type":"cond","areaPercentage":1,"length":30,"k":None,"materialID":"commonBrick-100mm"}
ID_R1= R1["materialID"]
length_R1=R1["length"]
originalLengthOfMaterial=materialLibrary[ID_R1]["length"]
OriginalRValueOfMaterial=materialLibrary[ID_R1]["RpValue"]
RValue_R1 = OriginalRValueOfMaterial*length_R1/originalLengthOfMaterial

R2={"name":"R2","type":"cond","areaPercentage":1,"k":None,"materialID":"commonBrick-100mm"}
ID_R2= R2["materialID"]



if (ID_R2 in AvailableMaterialIDs):
    
    if "length" in R2.keys():
        length_R2=R2["length"]
        originalLengthOfMaterial=materialLibrary[ID_R2]["length"]
        OriginalRValueOfMaterial=materialLibrary[ID_R2]["RpValue"]
        Rp_R2=OriginalRValueOfMaterial*length_R2/originalLengthOfMaterial
    else:
        OriginalRValueOfMaterial=materialLibrary[ID_R2]["RpValue"]
        Rp_R2=OriginalRValueOfMaterial
        print "pay attention that I used the originall length in library for this material"

        
        
else:
    print "I don't have a material called " +ID_R2+ " in my Library, Please enter k in your input"




Ri={"name":"Ri","type":"conv","area":12,"hconv":10}
Ro={"name":"Ro","type":"conv","area":12,"hconv":25}
R1={"name":"R1","type":"cond","area":12,"length":0.2,"k":0.8}
R2={"name":"R2","type":"cond","area":12,"length":0.3,"k":1.5}
R3={"name":"R3","type":"cond","area":12,"length":0.25,"k":0.54}
R4={"name":"R4","type":"cond","area":12,"length":0.35,"k":1.9}
R5={"name":"R5","type":"cond","area":12,"length":0.22,"k":0.78}
R6={"name":"R6","type":"cond","area":12,"length":0.31,"k":1.3}


resistances_in_series=[Ri,R1,Ro]

resistances_in_series_dictionary={"mode":"series","name":"resistanceInSeries","ReistanceList":resistances_in_series}
resistances_in_parallel_1=[R1,R2,R3]
resistances_parallel_1_dictionary={"mode":"parallel","name":"resistanceInParallel1","ReistanceList":resistances_in_parallel_1}
resistances_in_parallel_2=[R5,R6]
resistances_parallel_2_dictionary={"mode":"parallel","name":"resistanceInParallel2","ReistanceList":resistances_in_parallel_2}
wall_input_information = [resistances_in_series_dictionary,resistances_parallel_1_dictionary,resistances_parallel_2_dictionary]

R_wall = 0
for anyResistanceList_dictionary in wall_input_information:
    #print "\n \nHere is the next resistanceList dictionary "
    print "\n \n"
    print anyResistanceList_dictionary
    print "\n"
    resistanceListMode = anyResistanceList_dictionary["mode"]
    print "here is the mode of the current resistanceList "+resistanceListMode
    resistanceList= anyResistanceList_dictionary["ReistanceList"]
    print "\n Here you go!, here is our current resistance List! "
    print resistanceList
    for paolo in resistanceList:
        print "\n our Current paolo is :" 
        print paolo
    
    if resistanceListMode=="series":
        Rtotal_series=0
        Message="\n \n The Resistances are: \t"
        for resistance in resistanceList:
            #print "this is the resistance"
            #print resistance
            type_of_resistance=resistance["type"]
            #print "type of resistance is "+type_of_resistance
            A=resistance["area"]
            if type_of_resistance=="cond":
                L=resistance["length"]
                k=resistance["k"]
                R=round(float(L)/(k*A),4)
            elif type_of_resistance=="conv":
                A=resistance["area"]
                h=resistance["hconv"]
                R=round(1.0/(A*h),4)
            else:
                print "I don't know this type of resistance"
                break
            resistance["resistanceValue"]=R
            Rtotal_series=Rtotal_series+R
            Message=Message+str(R)+ " degC/W \t"
        R_wall=R_wall+ Rtotal_series
    elif resistanceListMode=="parallel":
        pass
        R_wall=R_wall+ R_parallel
        
        
    else:
        print "this mode does not exist"
        break

        

print "So the total resitance of your wall is: "+str(R_wall)+"degC/W"
Wall_information=[resistances_in_series,Rtotal_series]
wall_information_dictionary={"resistanceDetails":resistances_in_series,"Rtota_wall":Rtotal_series}


