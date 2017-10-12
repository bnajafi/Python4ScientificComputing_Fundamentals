A_string=raw_input("Please enter the area of the wall (in m2): ")
A=float(A_string)
NumberOfResistances_string=raw_input("Please enter number of resistances: ")
NumberOfResistances=float(NumberOfResistances_string)

R_tot=0
for ResistanceNumber in range(NumberOfResistances):
    print("\n \n \n Resistance Number "+ str(ResistanceNumber+1)+ "\n")
    ResistanceType=raw_input("Please choose the type of the resistance: conductive:1, convective=2 ")
    if ResistanceType=="1":
        print("\n this resistance is conductive")
        L=raw_input("Please Enter the length of the layer (in m): ")
        k=raw_input("Please Enter the condictivty of the layer (in W/(m*K)): ")
        print("\n you just said that in this layer "+ "L= " + L+ " m  "+ "k= "+ k +" W/(m*K) \n")
        R_resistance=float(L)/(float(k)*A)
        print("\n The Resistance's value is "+ str(R_resistance)+ " degC/W \n")
    if ResistanceType=="2":
        print("\n this resistance is conductive")
        h=raw_input("Please Enter the convective heat transfer coefficient (in W/(m2*K)): ")
        print("\n you just said that in this layer "+ "h= "+ h +" W/(m2*K) \n")
        R_resistance=1/(float(h)*A)
        print("\n The Resistance's value is "+ str(R_resistance)+ " degC/W \n")

    R_tot=R_tot+R_resistance
    ResistanceNumber=ResistanceNumber+1
print("\n We have calculated the resistance of all of the layers \n")
print("\n The Overall Resistance is "+ str(R_tot)+ " degC/W \n")

T_in_string=raw_input("Please enter the internal temperature (in degC): ")
T_out_string=raw_input("Please enter the ambient temperature (in degC): ")

DeltaT=float(T_in_string)-float(T_out_string)
Qdot=DeltaT/R_tot
print("\n The Heat Tranfer Rate is "+ str(Qdot)+ " W \n")
