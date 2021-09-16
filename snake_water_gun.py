def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 'g':
        if you == 's':
            return False
        else:
            return True
    elif (comp == 'w'):
        if (you == 'g'):
            return False
        else:
            return True
    else:
        if (you == 'g'):
            return True
        else:
            return False 
    

print("comp turn; select gun(g), snake(s), water(w)")

import random
random= random.randint(1,3)
#print(random)

if (random == 1):
    comp = 's'
elif (random == 2):
    comp='g'
else:
    comp='w'

you= input ("your turn; select gun(g), snake(s), water(w)")
print(f"comp chose {comp}")
print(f"you chose {you}")
d = gamewin(comp, you)
if (d == None):
    print("it was a tie")
elif d:
    print("you won")
else:
    print("you lose")









