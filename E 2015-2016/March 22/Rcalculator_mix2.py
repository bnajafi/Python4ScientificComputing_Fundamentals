RParallel = 0
RSeries = 0
anyParallel = raw_input("is there any parallel resistance? [y/n]")
if anyParallel == "y":
    numberOfParallel = raw_input("\n How many resistances are in parallel?")
    R_inv_parallel=0
    for resistance in range(numberOfParallel):
        type_resistance=raw_input(" \n what type of resistance is this? cond: condcutive, conv: convective")
        if type_resistance=="cond":
            print("\n this resistance is conductive")
            A_res_string=raw_input("please enter the area of the resistance in m2") #asking about the area
            L_res_string=raw_input("please enter the length of the resistance in m") #asking about the length
            k_res_string = raw_input("please enter the conductivity of the resistance in W/mK") #asking about the conductivity
            R_res = float(L_res_string)/(float(k_res_string)*float(A_res_string))
            print(" \n The resistance value of the present resistance is "+str(R_res)+" degC/W") 
        if type_resistance=="conv":
            print("\n this resistance is convective")
            A_res_string=raw_input("please enter the area of the resistance in m2") #asking about the area
            h_res_string = raw_input("please enter the convective heat transfer coefficient in W/m2K") #asking about the convective heat transfer coefficient
            R_res = 1/(float(A_res_string)*float(h_res_string))
            print("The resistance value fo the present resistance is "+str(R_res)+" degC/W")
        R_inv_parallel=R_inv_parallel+(1/R_res)
    RParallel=1.0/R_inv_parallel
    print("The overall resistance value of all parallel resistances is "+str(RParallel)+" degC/W")

anySeries = raw_input("is there any resistance in series? [y/n]")
if anySeries == "y":
    numberOfSeries = raw_input("How many resistances are in series?")
    resistanceNumber=0
    while resistanceNumber< (numberOfSeries):
        type_resistance=raw_input("what type of resistance is this? cond: condcutive, conv: convective")
        if type_resistance=="cond":
            A_res_string=raw_input("please enter the area of the resistance in m2") #asking about the area
            L_res_string=raw_input("please enter the length of the resistance in m") #asking about the length
            k_res_string = raw_input("please enter the conductivity of the resistance in W/mK") #asking about the conductivity
            R_res = float(L_res_string)/(float(k_res_string)*float(A_res_string))
            print("The resistance value fo the present resistance is "+str(R_res)+" degC/W")
        if type_resistance=="conv":
            A_res_string=raw_input("please enter the area of the resistance in m2") #asking about the area
            h_res_string = raw_input("please enter the convective heat transfer coefficient in W/m2K") #asking about the convective heat transfer coefficient
            R_res = 1/(float(A_res_string)*float(h_res_string))
            print("The resistance value fo the present resistance is "+str(R_res)+" degC/W")
        RSeries=RSeries+(1/R_res)    
        resistanceNumber += 1
    print("The overall resistance value of all resistances in series is "+str(RSeries)+" degC/W")
    
R_tot=RSeries+RParallel
        
    
    
        
            
            
            
            
