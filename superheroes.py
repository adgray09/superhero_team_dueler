import random


# would like to thank Cristian Lenberger for the help on my arena class


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
        return random.randint(0, self.max_block)

# certain hero 
class Hero:
    def __init__ (self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health
        self.deaths = 0
        self.kills = 0
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
    def defend(self):
        total_block = 0
        for block in self.armors:
            total_block += block.block()
        return total_block

    def take_damage (self, damage):
        self.current_health -= damage

    def is_alive (self):
        return self.current_health > 0

    def add_kills(self, num_kills=1):
        self.kills += num_kills

    def add_deaths(self, num_deaths=1):
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

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
        
        if (self.is_alive()):
            self.add_kills()
            opponent.add_deaths()
            print(self.name + ' Won the brawl!')
        elif (opponent.is_alive()):
            self.add_deaths()
            opponent.add_kills()
            print(opponent.name + ' Won the brawl!')
        else: 
            print("Draw!")

class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage//2, self.max_damage)

class Arena:
    def __init__ (self):
        self.tean_one: None
        self.team_two: None

        self.team_one = Team("team_one")
        self.team_two = Team("team_two")

    def create_ability(self):
        name = input("Name of your ability?\n")
        max_damage = input("Please enter the maximum damage of your ability.\n")
        new_ability = Ability(name, max_damage)
        return new_ability

    def create_weapon(self):
        weapon_name = input("Name of your weapon?\n")
        max_damage = input("Enter the maximum damage of your weapon.\n")
        new_weapon = Weapon(weapon_name, max_damage)
        return new_weapon

    def create_armor(self):
        armor_name = input("Name of your armor?.\n")
        max_block = input("Strength of armor?\n")
        new_armor = Armor(armor_name, max_block)
        return new_armor

    def create_hero(self):
        hero_name = input("Name of your hero?\n")
        hero_health = input("Health of your hero?\n")
        new_hero = Hero(hero_name, hero_health)
        return new_hero

    def build_team_one(self):
        num_heroes = int(input("How many heroes would you like on team one? "))
        self.team_one = Team(input("What would you like the team name to be? "))
        for _ in range(0, num_heroes):
            self.team_one.heroes.append(self.create_hero())
        
    def build_team_two(self):
        num_heroes = int(input("How many heroes would you like on team two? "))
        self.team_two = Team(input("What would you like the team name to be? "))
        for _ in range(0, num_heroes):
            self.team_two.heroes.append(self.create_hero())

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        team_one_total_kills = 0
        team_one_total_deaths = 0
        team_two_total_kills = 0
        team_two_total_deaths = 0
        for hero in self.team_one.heroes:
            team_one_total_kills += hero.kills
            team_one_total_deaths += hero.deaths
        for hero in self.team_two.heroes:
            team_two_total_kills += hero.kills
            team_two_total_deaths += hero.deaths
        
        team_one_ratio = team_one_total_kills / team_one_total_deaths
        team_two_ratio = team_two_total_kills / team_two_total_deaths
        print("Team ones K:D ratio: " + str(team_one_ratio))
        print("Team twos K:D ratio: " + str(team_two_ratio))

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

    def attack(self, other_team):

        while self.heroes and other_team.heroes:
            hero_1 = random.choice(self.heroes)
            hero_2 = random.choice(other_team.heroes)
            if hero_1.is_alive() and hero_2.is_alive():
                hero_1.fight(hero_2) 
        
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            if hero.is_alive() == False:
                hero.current_health = hero.starting_health

    def stats(self):
        for hero in self.heroes:
            ratio = hero.kills / hero.deaths
            print(hero.name + "'s KD ratio is" + ratio)
            
if __name__ == "__main__":

    running = True 
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    while running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            running  = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()


