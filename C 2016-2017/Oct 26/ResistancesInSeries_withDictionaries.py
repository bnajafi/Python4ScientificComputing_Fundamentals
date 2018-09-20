

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

for anyResistanceList_dictionary in wall_input_information:
    print "\n \nHere is the next resistanceList dictionary "
    #print anyResistanceList_dictionary
    resistanceListMode = anyResistanceList_dictionary["mode"]
    print "\n\nhere is the mode of the current resistanceList"+resistanceListMode

Rtotal_series=0
Message="\n \n The Resistances are: \t"
for resistance in resistances_in_series:
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
    #print Message
print Message
print "Here is some details about your resistances!: "
print resistances_in_series
print "So the total resitance of your wall is: "+str(Rtotal_series)+"degC/W"
Wall_information=[resistances_in_series,Rtotal_series]
wall_information_dictionary={"resistanceDetails":resistances_in_series,"Rtota_wall":Rtotal_series}


