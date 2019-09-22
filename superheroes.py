import random

class Ability:
    def  __init__ (self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    
    def attack(self):
        return random.randint(0, self.max_damage)
    

class Armor:
    def __init__ (self, name, max_block):
        self.name = name
        self.max_block = max_block
    
    def block (self):
        random.randint(0, self.max_block)

class Hero:
    def __init__ (self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health

if __name__ == "__main__":
   ''' armor = armor("breastplate", 10)
    ability = Ability("debugging ability", 20)
    print(Ability.name)
    print(Ability.attack())
    print(Armor.block)'''
my_hero = Hero("Alex Gray", 200)
print(my_hero.name)
print(my_hero.current_health)


