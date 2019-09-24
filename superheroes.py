import random

# adding ability
class Ability:
    def  __init__ (self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    
    def attack(self):
        return random.randint(0, self.max_damage)

# armor for hero
class Armor:
    def __init__ (self, name, max_block):
        self.name = name
        self.max_block = max_block
    
    def block (self):
        random.randint(0, self.max_block)

# certain hero 
class Hero:
    def __init__ (self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health
#adding ability to certain hero
    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack (self):
        dmg = 0 
        for abilities in self.abilities:
            dmg += abilities.attack()
        return dmg

# adding armor to certain hero 
    def add_armor (self, armor):
        self.armors.append(armor)
# defense
    def defend(self, damage_amt):
        total_defense = 0
        for hero in self.armors:
            total_defense += hero.block()
        return total_defense

    def take_damage (self, damage):
        self.current_health -= damage

    def is_alive (self):
        return self.current_health > 0

    def fight (self, opponent):
        print('A brawl is happening between  ' + self.name + ' and ' +
              opponent.name + '! Who will be victorious?')
        # choose first attacker
        fighter = random.randint(0, 1)
        rounds = 0
        while self.is_alive() and opponent.is_alive() and rounds < 200:
            if fighter == 0:
                damage = self.attack()
                print(damage)
                opponent.take_damage(damage)
                fighter = 0
            else:
                damage = opponent.attack()
                print(damage)
                self.take_damage(damage)
                fighter = 0
            print('{}: {} HP | {}: {} HP'.
                  format(self.name, self.current_health,
                         opponent.name, opponent.current_health))

class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage//2, self.max_damage)

class Team:
    def __init__ (self, name):
        self.name = name
        self.heroes = []

    def remove_hero (self, name):
        for hero in self.heroes:     
            if hero.name == name:
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

if __name__ == "__main__":

    #tests
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

