# -*- coding: utf-8 -*-
#Compound objects:
#Tuples
#List
#Dictionaries

#tuples
t1=(1,2,3,4)
t2=(1,3,7,"Gianluca")
t3=t1+t2
t4=5*t2
t5=(t1,5,8)
t6=(1,2,3,("Carlo","Gainluca"),6,"Paolo")
Resistances = (("glass",0.5,1.2),("brick",0.8,1.2))

#Lists A sequence of numbers that are mutable!
L1=[1,2,3,4]
L1[1]

L1[1]=9999
L2=["Paolo", L1, ("Matteo","Sara"),["Polimi","Polito"]]
L3=["JustAname","anotherName"]
L4=L2+L3

ResistanceList = [[0.8,0.2,12,"Resistance"],[1.8,0.3,12,"Resistance"]]
A=ResistanceList[0][2]
L=ResistanceList[0][1]
k=ResistanceList[0][0]
R=float(L)/(k*A)
ResistanceList[0][3]=R

A=ResistanceList[1][2]
L=ResistanceList[1][1]
k=ResistanceList[1][0]
R=float(L)/(k*A)
ResistanceList[1][3]=R

L1=[7,88, 12]


L10=range(1,10)
L11=range(10)


names=["Luca","Gianluca","Giusy Alessia"]
newNames=names
for student in names:
    print "Hi"+student
    index_student=names.index(student)
    newNames=newNames[index_student+1:]
    print index_student
    print newNames
    
    #
    #print names_copy
for student in names:
    print "Hi "+student
    index_student=names.index(student)
    newNames=newNames[index_student+1:]
    print index_student
    print newNames
names=newNames
    

names=["Luca","Gianluca","Giusy Alessia","Raffaele","Marco","Alice","Ratomir","Carlos","Daniel","Angela","Rıfat","Sadam","Caterina","Lorenzo","Nicolo","Giorgio"]
names=["Luca","Gianluca","Giusy Alessia"]
names_copy=names
names_copy.remove("Luca")
names_copy.append("Luca")

names=["Luca","Gianluca","Giusy Alessia"]
newNames=names
for student in names:
    print "Hi "+student
    index_student=names.index(student)
    newNames=newNames[index_student+1:]
    print newNames

Ri=["conv",12, 10]
Ro=["conv",12, 25]
R1=["cond",12,0.2,0.8]
R2=["cond",12,0.3,1.5]

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



        
    
        

A=R2[1]
L=R2[2]
k=R2[3]
R=round(float(L)/(k*A),4)
R2.append(R)



A=Ro[1]
h=Ro[2]
R=round(1.0/(A*h),4)
Ro.append(R)






    
    




