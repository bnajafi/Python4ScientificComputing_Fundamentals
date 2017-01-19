A=12 #m2
L=0.2 #m
k=raw_input("What is thr conductivity of this layer? ")
R=L/(float(k)*A)
print "The resistance of this layer is "+str(R)+ " degC/W"
