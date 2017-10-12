
Ri=["conv",12, 10]
Ro=["conv",12, 25]
R1=["cond",12,0.2,0.8]#Here is the order: 0:type, 1:area, 
R2=["cond",12,0.3,1.5]
R3=["cond",12,0.1,0.7]#Here is the order: 0:type, 1:area, 
R4=["cond",12,0.15,1.5]
R5=["cond",12,0.25,11.1]


#R_parallel=[R3,R4,R5]
#R_in Series=[Ri,Ro,R7,R8]

resistances_in_series=[Ri,R1,R2,Ro]
resistances_in_parallel=[R3,R4,R5]
Rtotal_series=0
Message="\n \n The Resistances are: \t"
for resistance in resistances_in_series:
    #print "this is the resistance"
    #print resistance
    type_of_resistance=resistance[0]
    #print "type of resistance is "+type_of_resistance
    A=resistance[1]
    if type_of_resistance=="cond":
        L=resistance[2]
        k=resistance[3]
        R=round(float(L)/(k*A),4)
        resistance.append(R)
        #print "Conductive resistance"
        #print resistance

    elif type_of_resistance=="conv":
        A=resistance[1]
        h=resistance[2]
        R=round(1.0/(A*h),4)
        resistance.append(R)
        #print "Conductive resistance"
        #print resistance

    else:
        print "I don't know this type of resistance"
        break
    Rtotal_series=Rtotal_series+R
    Message=Message+str(R)+ " degC/W \t"
    #print Message
print Message
print "So the total resitance of your wall is: "+str(Rtotal_series)+"degC/W"

Rtotal_parallel_inv=0
Message="\n \n The Resistances are: \t"
for resistance in resistances_in_parallel:
    #print "this is the resistance"
    #print resistance
    type_of_resistance=resistance[0]
    #print "type of resistance is "+type_of_resistance
    A=resistance[1]
    if type_of_resistance=="cond":
        L=resistance[2]
        k=resistance[3]
        R=round(float(L)/(k*A),4)
        resistance.append(R)
        #print "Conductive resistance"
        #print resistance

    elif type_of_resistance=="conv":
        A=resistance[1]
        h=resistance[2]
        R=round(1.0/(A*h),4)
        resistance.append(R)
        #print "Conductive resistance"
        #print resistance

    else:
        print "I don't know this type of resistance"
        break
    Rtotal_parallel_inv=Rtotal_parallel_inv+1/R
    Message=Message+str(R)+ " degC/W \t"
    #print Message
Rtotal_parallel=1/Rtotal_parallel_inv
print Message
print "So the total resitance of your wall is: "+str(Rtotal_parallel)+"degC/W"

R_total =Rtotal_parallel+Rtotal_series
