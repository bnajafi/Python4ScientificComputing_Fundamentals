
R1={"type":"convective","Area":15,"h_conv":10}
R2={"type":"conductive","length":0.004,"Area":1.2,"k":0.78}
R3={"type":"conductive","length":0.01,"Area":1.2,"k":0.09}
R4={"type":"conductive","length":0.004,"Area":1.2,"k":0.78}
R5={"type":"convective","Area":15,"h_conv":40}
R_network= [R1,R2,R3,R4,R5]

def Rcalc_Series(R_network):
    R_tot=0
    for R in R_network:
        print(str(R))
        if R["type"]=="conductive":
            print("\n this resistance is conductive") 
            print("\n In this resistance "+ "L= " + str(R["length"])+ " m  "+"A = "+str(R["Area"])+" m2"+ "k= "+ str(R["k"]) +" W/(m*K) \n")
            R_resistance=R["length"]/(R["k"]*R["Area"] )
            print("\n The Resistance's value is "+ str(R_resistance)+ " degC/W \n")
        if R["type"]=="convective":
            print("\n this resistance is convective") 
            print("\n In this resistanc"+ "A = "+str(R["Area"])+" m2"+ "h= "+ str(R["h_conv"]) +" W/(m*K) \n")
            R_resistance=1.0/(R["h_conv"] *R["Area"] )
            print("\n The Resistance's value is "+ str(R_resistance)+ " degC/W \n")  
    R_tot=R_tot+R_resistance
    print("\n We have calculated the resistance of all of the layers \n")
    print("\n The Overall Resistance is "+ str(R_tot)+ " degC/W \n")
            
    
Rcalc_Series(R_network)

