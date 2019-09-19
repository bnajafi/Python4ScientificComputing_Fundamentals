age = 29

if (age<18):
    print " just a teen"
elif age >=18 and age<25:
    print "enjoy it"
else:
    print "sorry, the slope is downwards!"
    
#LEt's create a conditional for external Rvalue
season  = "winter"
# You should never forget about the fact that equality is  ==  
# = is not equality !!!!! it is assignment

if season == "winter":
    RValue = 0.03
elif season == "summer":
    RValue = 0.044
else:
    print "you have not entered an acceptable season"

length = 55
if length == 90:
    RValue = 0.63
elif length == 140:
    RValue = 0.98
else:
    RValue = 0.63*float(length)/90
    print "I changed the standard value based on the new length"

Material_library = {"stucco":{"Rvalue":0.023,"length":13},"faceBreak_100mm":0.075,
"insideSurface":0.12,"outsideSurfaceSummer":0.044,"outsideSurfaceWinter":0.03
,"woodFiberboard_13mm":0.23}

layers_wall = ["faceBreak_100mm","woodFiberboard_13mm"]
# just optional !!
airOnTwoSides = ["insideSurface","outsideSurfaceWinter"]
layers_wall_complete = layers_wall + airOnTwoSides
# print "this layer is: "+ anyLayer
Rtot = 0
RValues_layers = []
for anyLayer in layers_wall_complete:
    RValue_layer = Material_library[anyLayer]
    Rtot=Rtot+RValue_layer
    RValues_layers.append(RValue_layer)
    print "this layer is: "+ anyLayer
    print "The value of R for this layer is: "+ str(RValue_layer)
    print "***************************************"
print "the total R Value is "+ str(Rtot)
    
    
# optional stuff
# how to include length in the library:
Material_library = {"stucco":{"Rvalue":0.023,"length":13},
"gypsum":{"Rvalue":0.13,"length":25} }

layers_wall = [{"material":"facebreak","legth":100},
{"material":"woodFiberboard","legth":13}
]

