print("\t\t\tEstimator of Battery life")
print("Program to estimate battery life")
print("Enter the Current Draw below and a list of batteries will be displayed\n")
I = float(input("Enter Current Draw: "))
print("\nPlease choose a battery from the list below: ")
print("1. AAA zinc-carbon")
print("2. AAA alkaline")
print("3. AA zinc-carbon")
print("4. AA alkaline")
print("5. C zinc-carbon")
print("6. C alkaline")
print("7. D zinc-carbon")
print("8. D alkaline")
battery = int(input("\nPlease enter the battery choice number, 1 through 8: "))
if battery == 1: #AAA zinc-carbon
    amphours = 0.2
if battery == 2: #AAA alkaline
    amphours = 0.5
if battery == 3: #AA zinc-carbon
    amphours = 0.4
if battery == 4: #AA alkaline
    amphours = 0.8
if battery == 5: #C zinc-carbon
    amphours = 1.5
if battery == 6: #C alkaline
    amphours = 3.2
if battery == 7: #D zinc-carbon
    amphours = 3.0
if battery == 8: #D alkaline
    amphours = 6.2                        



m = amphours / I
n = int(amphours // I)
b =amphours % I
minutes = int(b * 60)

if n == 0:
            n = m
            expectedLife = int(m * 60)
            print (f"Expected Life of battery = {expectedLife} minutes ")
elif n != 0:
            print ("Expected Life of battery = {} hours {} minutes".format(n,minutes))




