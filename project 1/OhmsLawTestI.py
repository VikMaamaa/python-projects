#Group 1, 2/5/2020 
print("\t\tCalculator for Current\n")
print("This program will determine the current given a voltage and resistance value")
V = float(input("What is the Voltage in volts? "))
R = float(input("What is the Resistance in ohms? "))
I = V/R
print("The current is {} amps".format(I))
print("\n\t\t\t{}ohms".format(R))
print("""\t\t|-------/\/\/\/-------|
\t\t|                     |
\t\t|                     |
\t\t|                     |
\t\t|        +    -       |
\t\t|--------[<---]-------|
""")
print("\t\t\t{}volts".format(V))
