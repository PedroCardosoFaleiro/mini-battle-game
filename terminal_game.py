import random

#HP
villain_life = 5
hero_life = 5
hero_shield = False

print("\nFight with the villain!\n")

while villain_life > 0 and hero_life > 0:
    print("-------------------------------------------\n")
    #Actions Hero
    print("Hero's turn:\n")
    print("1 - Hit")
    print("2 - Super hit")
    print("3 - Rest")
    print("4 - Protect")
    action = int(input("What is will you do? "))

    if hero_life >= 0:
        if action == 1: #Normal hit
            villain_life -= 1
            hero_shield = False
            print("You hit the villain!")

        elif action == 2: #Super hit / max damage
            villain_life -= 3
            hero_shield = False
            print("Super hit!")

        elif action == 3 : #heal
            hero_life += 2
            hero_shield = False
            print("You rested and recovered 2 life points.")

        elif action == 4: #will protect the next hit
            hero_shield = True
            print("You are protected from the next hit!")

        else:
            print("Invalid action!\n")
    
    if villain_life >= 0: #Está vivo?
        print("\n-------------------------------------------")
        #Actions Villain
        print("\nVillain's turn:\n")
        villain_action = random.randint(1,2)

        if villain_action == 1 and hero_shield == False: #Normal hit / Villain
            hero_life -= 1
            print("The villain hit you! Your life:", hero_life,"\n")

        elif villain_action == 1 and hero_shield == True: #Normal hit / Villain
            hero_shield = False
            print("The villain attacked, but you blocked it!\n")

        else:
            print("Miss\n")


print("\n-------------------------------------------")

if villain_life <= 0:
    print("Hero win")

elif hero_life <= 0:
    print("Villain wins!")