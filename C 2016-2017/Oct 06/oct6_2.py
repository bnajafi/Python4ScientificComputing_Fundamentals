L=raw_input("please enter the length: ") #Here I am just receiving the length from the user
A= raw_input("please enter the area: ")
k=raw_input("please enter the conductivity: ")
#k=0.9
# Now that I have all the data i can calculate R
"""
Here I am adding some comment lines 
comments line 1
comment line2

"""

R = float(L)/(float(k)*float(A))
print "You told me that the length of the layer is "+str(L)+" m "+" and the conductibity is "+str(k)+" W/mK"
print " \n So the resistance is \t"+ str(R)+ " degC/W"
