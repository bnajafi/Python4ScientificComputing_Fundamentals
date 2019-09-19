material = raw_input("please enter the material: ")
if material=="wood":
    k=1.1
elif material=="glass":
    k=0.78
elif material=="brick":
    k=1.5
else:
    k=float(raw_input("I dont know this material, please enter the conductivity"))
print "the value of k is "+str(k)+" W/mK"