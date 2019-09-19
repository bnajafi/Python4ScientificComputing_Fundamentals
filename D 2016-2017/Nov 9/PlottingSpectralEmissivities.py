
def spectralBlackBody(Lambda=0.7, T=5800):
    """ here is the explanation of this function"""
    import math 

    c0 = 2.9979*10**8 #m/s speed of light in vacuum
    h_Plank=6.626069*10**-34 #J.s Plank's Constant
    sigma_stefan_Boltzmann= 5.67*10**-8 #Stefan-Boltzmann Constant
    n=1 #the index of refraction of that medium
    c=c0/n# the speed of propagation of a wave in the medium 
    F=c/Lambda #the frequency of the wave
    e_wave=h_Plank*F
    E_blackBody = sigma_stefan_Boltzmann*T**4
    k_Boltzmann=1.38065*10**-23 #J/K Boltzmann Constant
    
    #Plank's Law: 
    C1=2*math.pi*h_Plank*c0**2*(10**24)#J*s*m^2/s^2--W*m2 --->W 
    C2=h_Plank*c0/k_Boltzmann*(10**6) #microm m/K

    EmissiveSpectral= C1/(Lambda**5*(math.exp(C2/(Lambda*T))-1))
    outPut = {"EmissiveSpectral":EmissiveSpectral,"E_blackBody":E_blackBody}
    return outPut
    
    
LambdaRange=[]
LNow=0.1
while LNow<5000:
    LambdaRange.append(LNow)
    LNow = LNow+ 0.01

T1=5800

EmissivePowerVector5800=[] 
for anyLambda in LambdaRange:
    spectralBlackBody_Result=spectralBlackBody(Lambda=anyLambda, T=T1)
    SpectralEmissivePower_current=spectralBlackBody_Result["EmissiveSpectral"]
    EmissivePowerVector5800.append(SpectralEmissivePower_current)
    
    
import matplotlib.pyplot as plt
plt.plot(LambdaRange,EmissivePowerVector5800,'r+')
plt.yscale('log')
plt.xscale('log')
plt.show()

    

