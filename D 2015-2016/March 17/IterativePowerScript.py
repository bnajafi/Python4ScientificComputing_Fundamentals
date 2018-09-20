def iterativePower(x,p):
    result=1
    for turn in range(p):
        result=result*x
        print("iteration "+str(turn)+ " Current Result "+str(result))
    return result
        
iterativePower(2,5)
        
