L=raw_input("What is the length of the layer (in m): ")
A=raw_input("What is the Area of the Material (in m2): ")#ask the area of the material
material=raw_input("Please Enter the material of the layer: ")# ask the material type
type_glas=raw_input("which type of glass do you mean:window=1, wool insulation=2 ")

if material=="glass" and int(type_glas)==1:
    k=str(0.96) #W/mK #the str denotes in letter form
elif material=="glass" and int(type_glas)==2:  
    k= str(0.04) #W/mK 
  
else:
    print("You have not provided sufficient data")   
print("\n you just said "+ "L= " + L+ " m  "+ "A= " + A+ " m2  "+ "k= "+ k +" W/(m*K) \n")
R=float(L)/(float(k)*float(A))
print("Well the Thermal Resistnace is "+ str(R)+ " degC/W")
