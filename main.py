from characters import Warrior, Monster

warrior= Warrior(50,5.5)
monster= Monster(150,10)

while warrior.health>0 & monster.health>0:
    choice=input(" Welcome Player.\n" \
    "What would you like to do today?\n" \
    "1) Attack.\n" \
    "2) Defend. \n" \
    "3) Cast spell. \n" \
    "4) End game.")

    if choice == "1":
        input