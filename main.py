"""
Cada heroi tem habilidades
Cada monstro tem diferentes habilidades, para cada habilidade do heroi

Usar Herança para uma clase de personagem e monstros

Usar polimorfismo Herois e monstros tem habilidades de ataques/defesa diferentes




OBJECTIVOS:

- Criação de classes para Herois com os seguintes atributos: NOME / VIDA / ATAQUE
- Criar subclasse para para os Herois: Warrior e Mage - Cada um com ataques diferentes - Espada e Magia respectivamente

- Criar classes para os mostros com os seguintes atributos: Nome / Vida / Ataque
- Criar subclass para os monstros: Dragão e Ogre - Dragões com resistência a magia e Ogres com resistencia a espadas


O objectivo do jogo será usar calculo para diferentes classes vs diferentes monstros até que um fique sem vida.

"""

#Import random module here
import random

#Basic stuff for characters like the monsters stuff and characters stuff  ---------- I use use the inheritance 

class Character:
    def __init__(self, name, weapon, health, damage):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.damage = damage
        
    #Creating attacks ---------- With random
    def attack(self, target):
        attack_damage = random.randint(1, self.damage) # The damage will be random
        target.taking_damage(attack_damage)
        print(f"{self.name} attacks {target.name} with {self.weapon} for {attack_damage} damage!")
        
    #Taking damage
        
    def taking_damage(self, damage):
        self.health -= damage
        if self.health <= 0: 
            print(f"{self.name}, You are dead. Insert coin")
        else :
            print(f"{self.name} has {self.health} health remaining.")
            
#Warrior class (From Character)        
        
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, "Sword",100, 20) #We have a name, health and damage of the sword
        print(f"\n I'm a Warrior of Light, and the people call me {name} I use my Sword to erase you from this life\n")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, "Staff",85, 30)
        print(f"\n I'm a Mage of Light, and the people call me {name} I use my Staff to erase you from this life\n")


class Dragon(Character):
    def __init__(self, name):
        super().__init__(name, "Fire Breath",200,35)
        print(f"\n I'm the Dragon of the Darkness, and my enemies call me {name} I use my Fire Breath to vanish you from this pity life\n")


class Ogre(Character):
    def __init__(self, name):
        super().__init__(name, "Bloody Axe",130,25)
        print(f"\n For THE HORDEEEEE, #$$$Q(/&/$%&) {name} &==)(((/)))  BLOODY AXE   §§§§§§§1112222#####\n")


#Battles ---------------- I used the Polymorphism

def battle(hero, monster):
    print("\nLet the battle begins!\n")
    
    #battle loop
    while hero.health > 0 and monster.health > 0 :
        #the hero will attack first
        hero.attack(monster)
        #If the monster doesnt die it will attack the hero
        if monster.health > 0:
            monster.attack(hero)
        
        if hero.health > 0:
            print(f"\n{hero.name} is victorious!")
        else:
            print(f"\n{monster.name} ended the world!!")


warrior1 = Warrior("Arthur")
mage1 = Mage("Merlin")
dragon1 = Dragon("BlackRoar")
ogre1 = Ogre("Orc")        

#battles - Here I create 2 battles 

battle(mage1, ogre1)
battle(warrior1, dragon1)