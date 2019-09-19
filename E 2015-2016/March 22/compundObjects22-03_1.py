# the fisrt type is tuple
t1=(1,2,3)
t2=("Gabriel",4,7,"Andrea",9)
t3 = t1+t2

t4=(t1,5,"Mario",6)
t5=(t2,t2,t3,9)

#the second type is list
names=["sara","andrea","John","babak","Juan"]
for name in names:
    print("Hi "+name)
k_materials=[0.9,0.87,1.2,3.5]
A=1.2
L=0.03
for k in k_materials:
    R=L/(k*A)
    print("the conductivity is "+str(k)+" so the resistance is "+str(round(R,4)))

L=[0.02,0.01,0.25,0.9]
A=[1.2,1.4,1.9,2.5]
k=[2.3,4.5,6.0, 9]


R1=["conductive",1.2,0.03,0.9] #R1[0]: type,R1[1]:area, R1[2]:length,R1[3]=conductivity
R1_k=R1[0]

#the third type is called a dictionary

Ri={"name":"Ri","type":"conv","area":0.25,"hConv":10}
R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
R2={"name":"R2","type":"cond","length":0.02,"area":0.25,"k":0.22}
R3={"name":"R3","type":"cond","length":0.16,"area":0.015,"k":0.22}
R4={"name":"R4","type":"cond","length":0.16,"area":0.22,"k":0.72}
R5={"name":"R5","type":"cond","length":0.16,"area":0.015,"k":0.22}
R6={"name":"R6","type":"cond","length":0.02,"area":0.25,"k":0.22}
Ro={"name":"Ro","type":"conv","area":0.25,"hConv":25}
R_parallel = [R3,R4,R5]
