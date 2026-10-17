class Human:
    def __init__(self,health):
        self.health =health
    def attack(self):
            print('attack')
    def take_damage(self,amount):
            self.health -= amount
            if self.health<0:
                self.health=0
                print(f' Remaining health : {self.health} hp')
    
    
class Warrior(Human):
    def __init__(self,health,defense):
        super().__init__(health)#super is use to call another class in order to use it's method
        self.defense=defense
    
    def defend(self):
        print(f'defend with {self.defense} defence')
    #Challenge 1: Adding a Method to Interact Between Objects
    
class Barbarian(Human):
    def __init__(self,health,damage):
        super().__init__(health)
        self.damage=damage
    def attack(self):
        print(f'attack with {self.damage} damage')

    
class Monster(Barbarian):
     def __init__(self,health,damage):
        super().__init__(health,damage) 
     def attack(self):
        super().attack()
     def __str__(self):
         return f"a monster with {self.health} hp"
    
#Challenge 2: Creating a Mage Class
class Mage(Human):
    def __init__(self,health,mana):
        super().__init__(health)
        self.mana=mana

    def cast_spell(self):
        print(f'mana is worth {self.mana} spells')


# warrior= Warrior(50,5.5)
# barbarian = Barbarian(100,8.1)
# monster = Monster(150,10)
# magee =Mage(80,100)  
# warrior.defend()
# warrior.take_damage(60)
# print(monster.health)
# print (monster)
# #Challenge 3: Polymorphism
# game_characters=[warrior, barbarian, monster]
# for characters in game_characters:
#     characters.attack()