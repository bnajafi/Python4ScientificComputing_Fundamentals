t1=(1,4,5)
t2=("Juan",4,6,7)
t3=t1+t2
t4=(t1,t2,5,6)
t1[0:2]
t2[0]
t4[1][1]
t4[3]=8 # tuple is not mutable

L1=[1,"Juan",3,5,"Sang"]
L2=[3,4,5]
L3=L1+L2
L4=[L1,3,4]
L4[1]
L4[0][1]
L4[0][1]= "Mattia"

Dict1={"userName":"user1","PassWord":"a123456","UserAge":29}
Dict2={1:"Conductive",2:"convective"}
Dict3={(1,2,3,4):"ClassAList"} #The key can be a tuple but not a list
Dict1["PassWord"]
Dict1["userName"]="user2" #so dictionary is mutable
Dict1["UserUniversity"]="Polimi"

