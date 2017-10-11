def powerOfN(x=2,n=3):
    """this function is completely useless, it just calculates x^n)"""
    y = x**n
    return y
    
result = powerOfN(2,5)

result = powerOfN(n=5,x=2)
result = powerOfN(n=10)

def wall_calc(listOfLayers):
    Material_library = {"stucco":{"Rvalue":0.023,"length":13},"faceBreak_100mm":0.075,
     "insideSurface":0.12,"outsideSurfaceSummer":0.044,"outsideSurfaceWinter":0.03
        ,"woodFiberboard_13mm":0.23}    
    airOnTwoSides = ["insideSurface","outsideSurfaceWinter"]
    layers_wall_complete = listOfLayers + airOnTwoSides
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
    results = {"Rtot":Rtot,"Rvalue of all layers":RValues_layers}
    return results
    
layers_wall = ["faceBreak_100mm","woodFiberboard_13mm"]
results_thisWall = wall_calc(layers_wall)