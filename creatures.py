from enum import Enum
import random

class Categories(Enum):
    
    Fire = 0
    Water = 1
    Grass = 2
    Rock = 3


class Creature:

    # constructor for object Creature
    
    def __init__(self, name, attack, hp, strong_against = None, weak_against = None, trainer=None):
        
        self.name = name
        while len(self.name) == 0:  # name = blank check
            self.name = input('Creature name cannot be empty, please provide a name :')
        self.attack = attack
        while self.attack > 10.0 or self.attack < 0:  # attack points must be in [0,10]
            self.attack = int(input('Creature AP cannot be more than 10 or less than 1. Provide new AP: '))

            
        self.hp = hp
        while self.hp > 20.0 or self.hp < 0:  # health points must be in [0,20]
            self.hp = int(input('Creature HP cannot be more than 10 or less than 1. Provide new HP: '))
        self.strong_against = strong_against
        self.weak_against = weak_against
        self.trainer = trainer
        
    # method returns all the information of a creature
    
    def to_string(self):
        
        if self.trainer is None:
            string = '--- Creature Information ---' + '\n' 
            string += '\n' +'Name: ' + self.name + '\n' + 'Attack Points: ' + str(self.attack) + '\n' + 'Health Points: ' + str(self.hp)
            string += '\n' + 'Is strong against: ' + str(self.strong_against) + '\n' + 'Is weak against: ' + str(self.weak_against) + '\n' + 'No Trainer' + '\n'
        else:
            string = '--- Creature Information ---' + '\n'
            string += '\n' +'Name: ' + self.name + '\n' + 'Attack Points: ' + str(self.attack) + '\n' + 'Health Points: ' + str(self.hp)
            string += '\n' + 'Is strong against: ' + str(self.strong_against) + '\n' + 'Is weak against: ' + str(self.weak_against) + '\n' + 'Trainer: '+ str(self.trainer.nick) + '\n'
        return string

    # method returns the attack points of a creature
    
    def get_attack(self):
        
        return 'Name: {} , Attack Points: {}'.format(self.name, self.attack)

    # method sets a given value to creatures attack points
    
    def set_attack(self, attack):
        
        while attack > 10.0 or attack < 0:  # loop that checks if AP's are in bounds
            print('\n' + 'Attack points must be in [0,10]' + '\n')
            attack = int(input('Provide new Attack points: ')) 
        else:
            self.attack = attack

    # method sets a trainer to a creature
    
    def set_trainer(self, master):
        
        self.trainer = master
        master.caught_creatures.append(self)

    # method returns the trainer of a creature
    
    def get_trainer(self):
        return self.trainer.nick

    #  method returns creatures health points

    def get_health(self):
        return self.hp

    # method checks amount of damage self will inflict on enemy based strong + weak against attributes

    def charge(self, enemy):
        if self == enemy:
            print('Cannot attack self')
        elif self.hp <= 0:
            print('Creature HP is low. Cannot attack')
        else:
            if self.is_strong_against(enemy):
                enemy.hp = enemy.hp - (2 * self.attack)
                if enemy.hp < 0:
                    enemy.hp = 0
            elif self.is_weak_against(enemy):
                enemy.hp = enemy.hp - (0.5 * self.attack)
                if enemy.hp < 0:
                    enemy.hp = 0
            else:
                enemy.hp = enemy.hp - self.attack


    def is_defeated(self):
        return self.hp <= 0


    # method checks if enemy.name  is in self.strong_against

    def is_strong_against(self, enemy):
        strong = False
        for tmp in self.strong_against:
            if tmp == str(type(enemy).__name__):
                strong = True
        return strong

    # method checks if enemy.name  is in self.strong_against

    def is_weak_against(self, enemy):
        weak = False
        for tmp in self.weak_against:
            if tmp == str(type(enemy).__name__):
                weak = True
        return weak

    def to_string_generator(self):
        string = 'Type: '+ type(self).__name__ + '\n' + 'Attack Points: ' + str(self.attack) + '\n' + 'Health Points: ' + str(self.hp)
        string += '\n' + 'Is strong against: ' + str(self.strong_against) + '\n' + 'Is weak against: ' + str(self.weak_against) + '\n'
        return string


class Fire(Creature):

    # Constructor of Fire subclass. Inherits constructor of parent Creature.

    def __init__(self, name, attack, hp, strong_against=None, weak_against=None, trainer=None):
        super().__init__(name, attack, hp, strong_against, weak_against, trainer=None)
        self.strong_against = [Categories.Grass.name]
        self.weak_against = [Categories.Rock.name, Categories.Water.name]
        self.trainer = trainer
        self.type = Categories.Fire


class Water(Creature):

     # Constructor of Water subclass. Inherits constructor of parent Creature.

    def __init__(self, name, attack, hp, strong_against=None, weak_against=None):
        super().__init__(name, attack, hp, strong_against, weak_against, trainer=None)
        self.strong_against = [Categories.Fire.name, Categories.Rock.name]
        self.weak_against = [Categories.Grass.name]
        self.type = Categories.Water


class Grass(Creature):

    # Constructor of Grass subclass. Inherits constructor of parent Creature.

    def __init__(self, name, attack, hp, strong_against=None, weak_against=None):
        super().__init__(name, attack, hp, strong_against, weak_against, trainer=None)
        self.strong_against = [Categories.Rock.name, Categories.Water.name]
        self.weak_against = [Categories.Fire.name]
        self.type = Categories.Grass


class Rock(Creature):

    # Constructor of Rock subclass. Inherits constructor of parent Creature.

    def __init__(self, name, attack, hp, strong_against=None, weak_against=None):
        super().__init__(name, attack, hp, strong_against, weak_against, trainer=None)
        self.strong_against = [Categories.Fire.name]
        self.weak_against = [Categories.Grass.name, Categories.Water.name]
        self.type = Categories.Rock


class Trainer:

    # constructor for the Trainer object
   
    def __init__(self, nick, xp, caught_creatures=None):
        
        self.nick = nick
        while len(self.nick) == 0:  # First name = blank check
            self.nick = input('First name cannot be empty, please provide a first name :')
        self.xp = xp
        if caught_creatures is None:
            self.caught_creatures = []
        else:
            self.caught_creatures.append(caught_creatures)

    # method returns all the information of a Trainer
    
    def to_string(self):
        
        caught = [] 
        for tmp in self.caught_creatures:
            caught.append(tmp.name)  # retuns the names of the object's Creatures in a list 
        string = 'First name: ' + self.nick
        string += '\n' + 'XP Points: ' + str(self.xp) + '\n' + 'Caught creatures: ' + str(caught) + '\n'
        return string

    # method which returns the nickname of the Trainer
    
    def get_call_sign(self):
        
        return self.nick

    # method on how a trainer catche's a Creature

    def catch(self, enemy):
        if enemy in self.caught_creatures:
            print('Cannot catch self')
        else:
            if enemy.hp <= 2:  # To catch enemy , enemy.hp must be <=2 
                print('Creature caught!' + '\n')  # I create some white space so the output is easier to read
                self.caught_creatures.append(enemy)
                enemy.trainer = self  # Change the enemy trainer to self.trainer
                self.xp += 2  
            else:
                print('Creature HP is to high')

    # boolean method to check if a Trainer is defeated. Defeat is True when all of the caught_creatures have 0 health points 

    def is_defeated(self):
        
        dead = True
        for tmp in self.caught_creatures:
            if tmp.hp:
                dead = False
        return dead
     
    # method to choose a creature from the caught creatures of the Trainer object

    def choose(self):
        
        caught_backend = {}  # This is a dictionary which connects the names of the objects (keys) with the self.obejcts (values). Not visible to the user
        caught_user = []  # This is a list visible to the user containing the names of the caught creatures as well as their HP points
        for tmp in self.caught_creatures:
            if tmp.hp > 0:  # Since its a choose a creature method we need to check if creature health > 0.
                caught_backend.update({tmp.name : tmp})  # tmp.name is the name of the object and tmp is the object
                caught_user.append(tmp.name + ', ' + 'Health: ' + str(tmp.hp))  # Users list
        if len(caught_backend) != 0:  
            print(caught_user)
            name = input('Type the name of the creature you want to use, from the list above: ' + '\n')
            while name not in caught_backend:
                print(caught_user)
                name = input('Invalid name. Please type a name from the list above: ' + '\n')
            return caught_backend[name]  # returns the object itself 
            
# function to initialize a list containing Creatures(Objects) with their type so the user can choose the preferd type for the 1st creature.

def creature_generator(name):
    
    cr_list = [Fire(name, 5 , 15), Water(name, 5 , 15), Rock(name, 5 , 15), Grass(name, 5 , 15)]
    for i in cr_list:
        print(i.to_string_generator())
    return cr_list

def enemy_generator(name):
    
    cr_rand_en = [Fire(random.choice(name), random.randint(0, 10), random.randint(10,20)), Water(random.choice(name),random.randint(0, 10), random.randint(10,20)), Rock(random.choice(name),  random.randint(0, 10) , random.randint(10,20)), Grass(random.choice(name),  random.randint(0, 10) , random.randint(10,20))]
    return cr_rand_en

# check if a str is ''

def is_blank(value):
    if len(value) == 0 or value[0] == ' ':
        return True
    else:
        return False


# main game loop idea. can be customized for any game.

def game_loop():
    
    random_names = ['Bulbasar', 'Charmander', 'Mioutou', 'Vagos']
    username = str(input('Please provide a name for your Trainer: '))  # name of the trainer
    while is_blank(username):
        username = str(input('\n'+'Name cannot be blank. Give a new name: ' ))
    trainer_user = Trainer(username,0)  # plugs the user variable into the Trainer constructor self.name = user
    name = str(input('\n' + 'Choose name for your first Creature : ' ))  # name of the 1st creature
    while is_blank(name):
        name = str(input('\n'+'Name cannot be blank. Give a new name: ' ))
    starting = creature_generator(name)  # plugs the name var into the creature_gen func which creates a list with objects Creatures and the 4 types
    kind = str(input('\n'+'Choose the type of your creature by typing it: '))
    found = 0
    while True:
        for i in starting:  # i becomes object creture
            if kind == type(i).__name__:  # check if users input is in starting. Note that starting contains objects so we need to check if the input == name of object
                cr_1 =  i
                found = 1
        if found:
            break
        else:
            kind = input('\n' + 'Invalid name. Type: Fire, Water, Grass or Rock:  ')
    cr_1.set_trainer(trainer_user)        
    print('This is your Trainer: ' + '\n')
    print(trainer_user.to_string())
    cr_enemy = enemy_generator(random_names) # sets a 1st enemy
    play = input('\n' + 'Type yes if you want to start playing else type no: ')
    
            
            
def main():
    
    game_loop()

if __name__ == '__main__':
    main()
