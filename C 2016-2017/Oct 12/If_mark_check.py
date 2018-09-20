mark=int(raw_input("please enter your mark: "))
if mark<18:
    result="fail"    
elif (mark>=18 and mark<=24):
    result= "good"
else:
    result="exellent"
print "your result is "+ result
    