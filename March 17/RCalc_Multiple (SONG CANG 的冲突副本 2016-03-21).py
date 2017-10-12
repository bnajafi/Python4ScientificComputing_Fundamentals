def Rcalculator():
    A_string=raw_input("Please enter the area of the wall (in m2): ")
    A=float(A_string)
    NumberOfLayers_string=raw_input("Please enterNumber of layers: ")
    NumberOfLayers=int(NumberOfLayers_string)
    layerNumber=1
    R_tot=0
    
    for j in range(1,NumberOfLayers+1):#range will start from 0 but less than 1 the final 3
    print("\n \n \n Layer Number "+ str(layerNumber)+ "\n")
    Materialtype=raw_input("is it conductive==1 or convective==2")# ask is material is conductive or convective
    
    if Materialtype==str(1):
        print("this ty is conductive")
        L=raw_input("Please Enter the length of the layer (in m): ")
        k=raw_input("Please Enter the condictivty of the layer (in W/(m*K)): ")
        print("\n you just said that in this layer"+ "L= " + L+ " m  "+ "k= "+ k +" W/(m*K) \n")
        R_layer=float(L)/(float(k)*A)
        R_tot=R_tot+R_layer
        print("\n The layer's Resistance is"+ str(R_layer)+ " degC/W \n")
        layerNumber=layerNumber+1
        
    elif R_tote==str(2):# showing that the material is not conductive
        
        h=raw_input("Please Enter the heat transfer coef (in W/(m2*K)): ")
        print("\n you just said that in this layer"+ "h= " + h+ " W/m2K  ")
        R_layer=1/(float(h)*A)
        R_tot=R_tot+R_layer
        print("\n The layer's Resistance is"+ str(R_layer)+ " degC/W \n")
        layerNumber=layerNumber+1
        
    print("\n We have calculated the resistance of all of the layers \n")
    print("\n The Overall Resistance is "+ str(R_tot)+ " degC/W \n")
return R_tot

Rcalculator()
