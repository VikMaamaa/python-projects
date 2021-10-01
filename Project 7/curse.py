import random

Noun = ('Goat','Fool','Thief','Bastard','Dog','Fish','Idiot','asshole','bitch','nigga','empty brain','gold digger')

Adjective = ('Ugly', 'poor', 'Sweet', 'Red', 'Black', 'Bitter',
             'wonderful', 'gentle', 'unfortunate', 'sleepy', 'foolish', 'quick',
             'Crazy','stupid','rotten','stubborn')

print("-"*60 +"\n\t\tProgram to generate random curses\n" + "-"*60)
NumCurses = int(input("\nEnter number of curses: "))
for Curse in range(NumCurses):
    def goback():
        ad1 = random.randrange(len(Adjective))
        ad2 = random.randrange(len(Adjective))
        if ad1 != ad2:
            n = random.randrange(len(Noun))
            print("You",Adjective[ad1],Adjective[ad2], Noun[n])
            print("+"*60 + "\n"+"_"*60 +"\n")
        else:
            goback()
    goback()        







    

