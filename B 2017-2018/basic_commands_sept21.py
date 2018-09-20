L = 0.008 # thickness of glass 
A = 1.5*0.8 # area of the window
k = 0.78 # conductivity of glass

R = L/(k*A) #calculating the resistance
print R
print(R)


# strings !!!!
name = "marco"
name2 = 'marco'

# these two methods are the same!

# concatenation

name1= "marco "
name2 = "sara"

names = name1+name2

result = "the answer is "+ str(2.7)
# type casting 
number_conv = str(10.5)
check = float(number_conv)+5 
check2 = number_conv+ str(5)

# Let's make our calculations prettier

L = 1 # thickness of glass, in m 
A = 2 # area of the window in m2
k = 1 # conductivity of glass in W/m.K
L = float(L)
R = L/(k*A) #calculating the resistance
print "you just told me that"+" the thickness is "+str(L)+" m2 "+ "and the conductivity is "+str(k)+ " W/mK"+ "so-->" 
print "The resistance or the layer is "+str(R)+ " (degC/W)"

#String oeprations !
name = "Marco"
letter_2 = name[1]
letter_last = name[4]

# second way!!
letter_last = name[-1]

# how to take a slice!
letters = name[1:3] # the last number you write is not included !!

name2="Gianluca"
letters2= name2[3:5]

# how to take parts
letters3 = name2[4:] # here you don't use end like matlab
letters4 = name2[:4] # it does not inlcude the last letter!!!

long_string= 5*"python " # string multiplication7

# How to receive a value from the user! raw_input
L = float(raw_input("please enter the length in m "))
A = float(raw_input("please enter the length in m2 "))
k = float(raw_input("please enter the conductivity in w/mK "))
R=L/(k*A)
print "the resistance is "+str(R)+ " degC/W"
