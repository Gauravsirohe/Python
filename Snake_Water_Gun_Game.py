#Snake Water Gun Game
#Craeted by Kumar, Gaurav
#Date: 06 August, 2022

import random   
def game(comp, you):
        
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
           return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False
        
rnd = random.randint(1,3)

if rnd==1:
    comp='s'
elif rnd==2:
    comp='w'
elif rnd==3:
    comp='g'

print("Computer turn: Snake(s) Water(w) or Gun(g)?", comp)

you = input("Your turn: Snake(s) Water(w) or Gun(g)? ")


print(f"Computer choose {comp}")
print(f"Your choose {you}")

if (you=='s' or you=='w' or you=='g'):
    result = game(comp,you)
    if result == None:
        print("Tie")
    elif result:
        print("You win")
    elif result:
        print("You loose")
else:
    print("This is not applicable. Choose correct option as s,w or g")
