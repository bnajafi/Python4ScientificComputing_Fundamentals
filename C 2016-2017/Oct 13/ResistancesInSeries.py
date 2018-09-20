
Ri=["conv",12, 10]
Ro=["conv",12, 25]
R1=["cond",12,0.2,0.8]
R2=["cond",12,0.3,1.5]

#R_parallel=[R3,R4,R5]
#R_in Series=[Ri,Ro,R7,R8]

resistances_in_series=[Ri,R1,R2,Ro]
Rtotal=0
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
    Rtotal=Rtotal+R
    Message=Message+str(R)+ " degC/W \t"
    #print Message
print Message
print "So the total resitance of your wall is: "+str(Rtotal)+"degC/W"
