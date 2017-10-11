
T1 = 37+273
T2 = 17+ 273

Tm= (T1+T2)/2
F = 1
sigma = 5.67*10**-8

Qdot_per_area_1 = sigma*F*(T1**4-T2**4)

# Method2 
hrd= 4*sigma*F*Tm**3


Qdot_per_area_2 = hrd*(T1-T2)

Error_percent= (Qdot_per_area_2-Qdot_per_area_1)/Qdot_per_area_1*100