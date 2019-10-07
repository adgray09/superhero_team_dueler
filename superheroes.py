import random


# would like to thank Cristian Lenberger for the help on my arena class as well as the team testing. Had to find errors in pasted code from tutorial.


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
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
#adding ability to certain hero
    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack (self):
        dmg = 0 
        for ability in self.abilities:
            dmg += ability.attack()
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
        if damage - self.defend() > 0:
            self.current_health -= (damage - self.defend())
            print(self.name + " HP: " + str(self.current_health))
        else:
            print("The attack was blocked")
            print(self.name + " HP: " + str(self.current_health))

    def is_alive(self):
        if int(self.current_health) > 0:
            return True
        else: 
            return False

        
    def add_kills(self, num_kills=1):
        self.kills += num_kills

    def add_deaths(self, num_deaths=1):
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def fight (self, opponent):
        print('A brawl is happening between  ' + self.name + ' and ' +opponent.name + '! Who will be victorious?')
        # choose first attacker
        while self.is_alive() and opponent.is_alive():
            if self.abilities or opponent.abilities:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            else:
                print("DRAW!")
        if self.current_health <= 0:
            print(opponent.name + " is the winner!")
            opponent.add_kills(1)
            self.add_deaths(1)
            
        else:
            print(self.name + " is the winner!")
            self.add_kills(1)
            opponent.add_deaths(1)
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
    def __init__(self, name, max_damage):
        super().__init__(name, max_damage)
    
    def attack(self):
        return random.randint(self.max_damage//2, self.max_damage)

class Arena:
    def __init__(self):
        self.team_one: None
        self.team_two: None

    def create_ability(self):
        name = input("Enter the name of the heroes ability: ")
        max_damage = int(input("Enter the maximum damage of the heroes ability: "))
        new_ability = Ability(name, max_damage)
        return new_ability

    def create_weapon(self):
        name = input("Enter the name of the heroes weapon: ")   
        max_damage = int(input("Enter the maximum damage of the heroes weapon: "))
        new_weapon = Weapon(name, max_damage)
        return new_weapon

    def create_armor(self):
        name = input("Enter the type of heroes armor: ")
        max_block = int(input("Please enter the maximum block of the heroes armor: "))
        new_armor = Armor(name, max_block)
        return new_armor

    def create_hero(self):
        name = input("Enter the name of your hero: ")
        starting_health = int(input("Enter the starting health of your hero: "))
        new_hero = Hero(name, starting_health)
        num_abilities = int(input("How many abilities does your hero have? "))
        for _ in range(0, num_abilities):
            new_hero.add_ability(self.create_ability())
        num__weapons = int(input("How many weapons does your hero have? "))
        for _ in range(0, num__weapons):
            new_hero.add_weapon(self.create_weapon())
        num_armor = int(input("How many armors does your hero have? "))
        for _ in range(0, num_armor):
            new_hero.add_armor(self.create_armor())
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


