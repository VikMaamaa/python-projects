#Group1
#program to calculate specification of resistor when given the resistance value
#tolerance and value
tol = float(input("Enter the percentage tolerance (%): "))/100.0
Rnominal = float(input("Nominal value (ohms): "))
Rmeasured = float(input("Measured value (ohms): "))

Roffset = Rnominal * tol
Rupper = Rnominal + Roffset
Rlower = Rnominal - Roffset

if (Rmeasured >= Rlower and Rmeasured <=Rupper):
    print("This device is within tolerance.")
if (Rmeasured < Rlower or Rmeasured > Rupper):
    print("This device is out of tolerance.")

Actualdev = float(100.0 * (Rmeasured - Rnominal) / Rnominal)

print("The actual deviation is {} percent".format(Actualdev))

