
#Group 1, 2/5/2020
print("\t\tCalculator for Resistance\n")
print("This will determine the resistance given a current and voltage value")
V = float(input("What is the Voltage in Volts? "))
I = float(input("What is the Current in amps? "))
R = V/I
print("The resistance is {} ohms".format(R))
print("\n\t\t\t{}ohms".format(R))
print("""\t\t|-------/\/\/\/-------|
\t\t|                     |
\t\t|                     |
\t\t|                     |
\t\t|        +    -       |
\t\t|--------[<---]-------|
""")
print("\t\t\t{}volts".format(V))
