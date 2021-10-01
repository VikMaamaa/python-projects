import random


print("\t\t\tMiniature Monte Carlo Simulator")
print("Program to determine the voltage across the second resistor R2")
E = float(input("\nEnter the value of Voltage Source in Volts: "))
R1 = float(input("Enter the resistance of R1 in Ohms: "))
Tol1 = float(input("Enter the percent tolerance of R1: "))
Tol1 = Tol1/100.0 #Turn this from a percentage into a factor

R2 = float(input("\nEnter the resistance of R2 in ohms: "))
Tol2 = float(input("Enter the percent tolerance of R2:"))
Tol2 = Tol2/100.0 #Turn this from a percentage into a factor
#Randomized value Calculation for R1
R1max = R1 + R1 * Tol1
R1min = R1 - R1 * Tol1
R1rand = R1min + (R1max - R1min) * random.random()
#Randomized value Calculation for R2
R2max = R2 + R2 * Tol2
R2min = R2 - R2 * Tol2
R2rand = R2min + (R2max - R2min) * random.random()
#Voltage across R2
VR2 = E * R2rand / (R1rand + R2rand)
print(f"\nRandomized R1 value is {R1rand} ohms")
print(f"Randomized R2 value is {R2rand} ohms")
print(f"\nThe Voltage across R2 is {VR2} volts")
