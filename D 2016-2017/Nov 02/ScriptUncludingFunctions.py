def myPowerCalc(x=2,a=4):
    """This is a useless function we made to practice defining functions in python"""
    y=x**a
    zz = y+2
    myResult = {"y":y,"zz":zz}
    return myResult
    
SomeNumber=50
x=2  
Result = myPowerCalc(2,3)["y"]

inputs = {"input1":3,"input2":2}
def myPowerCalc2(carlos):
    x = carlos["input1"]
    a = carlos["input2"]
    y=x**a
    zz = y+2
    myResult = {"y":y,"zz":zz}
    return myResult

results_of_inputs = myPowerCalc2(inputs)
    
    
