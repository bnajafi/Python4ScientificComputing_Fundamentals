L=raw_input("Please Enter the length of the layer (in m): ")
A=raw_input("Please Enter the area of the wall (in m2): ")
material=raw_input("Please Enter the material of the layer: ")

if material=="glass":
    type_glas=raw_input("which type of glass do you mean:window=1, wool insulation=2 ")
    if int(type_glas)==1:
        k=str(0.96) #W/mK
    elif int(type_glas)==2:
        k= str(0.04) #W/mK 
    else:
        print("The selected glass type is not acceptable")
       
        
elif material=="brick":
    k=str(0.8) #W/mK
   
else:
    print("I do not have the properties of this material")
    k=(raw_input("Please Enter the conductivity off the layer(in W/(m K):  "))
print("\n you just said "+ "L= " + L+ " m  "+ "A= " + A+ " m2  "+ "k= "+ k +" W/(m*K) \n")
R=float(L)/(float(k)*float(A))
print("Well the Thermal Resistnace is "+ str(R)+ " degC/W")
