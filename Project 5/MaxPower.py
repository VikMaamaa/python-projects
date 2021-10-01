#Maximun Power transfer Theorem Visualization
print("\t\tMaximum Power Transfer Theorem Visualization")
print("\nEnter the values of source voltage and its internal resistance")
E = float(input("\nEnter the Source Voltage in volts: "))
Rsource = float(input("Enter the Internal Resistance of Voltage Source: "))
Pmax = 0
print("\nRload\t\tVload\t\tI\t\tPload")
Rload = 0.1*Rsource
while Rload < 2.0*Rsource:
    I = E/(Rsource + Rload)
    Vload = E * Rload/(Rsource + Rload) 
    Pload = I * Vload
    if Pload > Pmax:
        Pmax = Pload
    print("%.4e\t%.4e\t%.4e\t%.4e"%(Rload,Vload,I,Pload))      
    Rload += 0.1*Rsource
   
print("\n\tMaximum Power found is {}".format(Pmax))    
sf = int(50.0/Pmax)

#Section for Graph
print('\n\t',"*"*60)
print("\n\t\tGraph of Load Power versus Load Resistance")
print("\n\t","*"*60)
Rload = 0.1*Rsource
while Rload < 2.0*Rsource:
    I = E/(Rsource + Rload)
    Vload = E * Rload/(Rsource + Rload) 
    Pload = I * Vload
    if Pload > Pmax:
        Pmax = Pload
    print("%.4e"%(Rload),"t\t",int(Pload*sf)*"*")    
    Rload += 0.1*Rsource       
