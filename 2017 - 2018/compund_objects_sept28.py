str1 = "LucaMarcoSara"
First_letter= str1[0]
Last_letter= str1[-1]
JustFirstName=str1[0:4]
newName= "Ali"
names= str1+newName

# Lists []
L1 = [2,5,"Luca",9] #first list
L2 = [3,8,7] #second list
L3 = L1+L2 #concatenation

name2=L1[2]
lastOne=L1[-1]
twoElements= L1[1:3]

Resistance = ["cond",1.5,0.008,0.78] # glass layer 



#Second compound object tuple ()
t1 = (4,5,6,7)
t2= (8,9,10,999)
t3=t1+t2
t3[0]
t3[1]=2000
# We don't usually use tuple!! because tuples are immutable 


# List assignment

L3[3]=1000
#L3[7]=3000 #You can't do this!!!!
# List methods 
L3.append(3000)

names = ["luca","matteo","Manoj","Tarun","Ali"]


# For loop
for name in names:
    print "Hi "+name
print "I am not inside the loop"

resistance_values = [0.003,0.03,0.05,0.1]
total_res = 0
for resistanceValue in resistance_values:
    total_res=total_res+resistanceValue
    print "resistance Value is"+str(resistanceValue)
print "total resistance is"+str(total_res)

     
R1 = [1.5,0.008,0.78] # glass layer 1, Area:0,Length 1, conductivity 2
R2 = [1.5,0.01,0.08] # air gap
R3 = [1.5,0.004,0.78] # glass layer 2

L_R1= R1[1]
A_R1 = R1[0]
k_R1=R1[2]
RValue_R1 = L_R1/(A_R1*k_R1)

ListOfResistances = [R1,R2,R3]
totalResValue= 0
for anyResistance in ListOfResistances:
    print "here is the new resistance:"
    print anyResistance
    L_anyResistance= anyResistance[1]
    A_anyResistance = anyResistance[0]
    k_anyResistance=anyResistance[2]
    RValue_anyResistance = L_anyResistance/(A_anyResistance*k_anyResistance)
    totalResValue = totalResValue+RValue_anyResistance
    print "so the calculated resistance is: "+str(RValue_anyResistance)
    print "***********"
print "so the total Resistance is: "+str(totalResValue)

#dictionaries

student1 = {"name":"Marco","university":"Polimi"}
R1 = {"area":1.5,"length":0.008,"conductivity":0.78}
area_R1=R1["area"]


# Now let's do that using dict
 

R1= {"name":"glass 1","area":1.5,"length":0.008,"k":0.78,"ResValue":0}
R2= {"name":"air gap","area":1.5,"length":0.01,"k":0.08,"ResValue":0}
R3= {"name":"glass 2","area":1.5,"length":0.004,"k":0.78,"ResValue":0}

L_R1= R1["length"]
A_R1 = R1["area"]
k_R1=R1["k"]
RValue_R1 = L_R1/(A_R1*k_R1)

ListOfResistances = [R1,R2,R3]
totalResValue= 0
for anyResistance in ListOfResistances:

    L_anyResistance= anyResistance["length"]
    A_anyResistance = anyResistance["area"]
    k_anyResistance=anyResistance["k"]
    name_anyResistance = anyResistance["name"]
    RValue_anyResistance = L_anyResistance/(A_anyResistance*k_anyResistance)
    anyResistance["ResValue"]=RValue_anyResistance
    print "here is the new resistance:"
    print anyResistance
    totalResValue = totalResValue+RValue_anyResistance
    print "so the calculated resistance for "+name_anyResistance+" is "+str(RValue_anyResistance)
    print "***********"
    
print "so the total Resistance is: "+str(totalResValue)

