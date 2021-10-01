#This is a program for the battle game


import random
lives = 5; score = 0; sn_weapon = 0
print("""
************************************************************
* \t   .''''.         ...         ...   ...     _____  *
*   \t  /~    ~\        |  ;    /\  |  ;  |  ;  |   |    *
*  \t(|.@    @.|)      |''.   /__\ |.'.  |.'.  |   |    *
*   \t  (      )        |   } /    \|...' |...' |   |    *
*   \t   /(  )\                                          *
*     \t     ..                                            *
************************************************************
    """)
print("While in a battle field, you come across a dangerous rabbit")
print("that attacked you....................... \n")


weapon_menu = ["Sword","Dagger","Holy Hand Grenade of Antioch",
               "catapult","shrubbery",]

print("#########********* Weapon Menu *********#########")
for choice in weapon_menu:
    sn_weapon +=1
    print(f"\t{sn_weapon}.       {choice}")

while lives > 0:
    #main battle loop
    print("-"*45)
    print("Remaining lives: {}\t\t score: {}".format(lives,score))
    print("-"*45)
    weapon = int(input("Choose a weapon 1-{}: ".format(len(weapon_menu))))
    print("\n\n\n")
    r = random.randrange(100)
    if weapon == 1: #rock
        if r< 10: #10% chance to win
            print("You killed the rabbit!")
            score += 500
        else:
            print("You died an embarrasing death: rabbit food!!!")
            lives -= 1
    elif weapon == 2: #lance
        if r<15: #15% winning odds
            print("The rabbit has been vanquished!!")
            score +=200
        else:
            print("Fool!! You ended your days as an appetizer!")
            lives -= 1
    elif weapon == 3: #grap
        if r<60: #60% winning odds
            print("The rabbit couldn't bear the pain!!! voooommm!!!\nit ran into tin space!!!")
            score +=600
        else:
            print("The chances of running became higher..")
            lives -= 1
    elif weapon == 4: #trap
        if r<70: #70% winning odds
            print("The rabbit was torn into pieces!!")
            score +=700
        else:
            print("Your existence couldn't be traced!!!! You're dead!!!")
            lives -= 1
    elif weapon == 5: #finale
        if r<80: #80% winning odds
            print("You ended up using the rabbit for a delicious meal")
            score +=800
        else:
            print("You really tasted nice, says the rabbit!!!!")
            lives -= 1
    elif weapon >= len(weapon_menu):
        print("Invalid weapon selected")
print("Total score: {}".format(score))
if score>=1200:
    print("\n\n","++"*10,"CONGRATULATIONS!!!!!!","++"*10)
print("-"*60,"\n\t\tGame Over\n","-"*60,"\n")



