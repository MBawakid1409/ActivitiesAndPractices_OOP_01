# Activities & Practices
# --------- [OOP] ---------
from random import random


print("--------- [OOP] ---------")
print("----------------------------------")
# Practise 01
print("Practise #01")
print("Creating a Dog Class")

class Dog:
  def __init__(self, input_name, input_breed, input_age = 0, input_friendliness = True):
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_friendly = input_friendliness
    self.friends = []

  def have_birthday(self):
    self.age = self.age + 1
    print("{name} had a birthday! {name} is {age} years old.".format(name = self.name, age = self.age))  

  def become_friends(self, other_dog):
    if other_dog.is_friendly:
      self.friends.append(other_dog)
      other_dog.friends.append(self)
      print("{name} become friends with {other_name}!".format(name = self.name, other_name = other_dog.name))
    else:
      print("{other_name} did not want to become friends with {name}!".format(name = self.name, other_name = other_dog.name))

  def __repr__(self):
    description = "This {breed} named {name} is {age} years old and has {number_of_friends} friend/s.".format(breed = self.breed, name = self.name, age = self.age, number_of_friends = len(self.friends))
    if self.is_friendly:
      description += " {name} is friendly dog.".format(name = self.name)
    else:
      description += " {name} is an unfriendly dog.".format(name = self.name)
    return description    


dog_one = Dog("Sparky", "Golden Retriever", 5)
dog_two = Dog("Bruno", "Chihuahua", 10, False)

dog_one.have_birthday()
# Output: Sparky had a birthday! Sparky is 6 years old.
# dog_one.become_friends(dog_two)
# Output: Bruno did not want to become friends with Sparky!
dog_two.become_friends(dog_one)
# Output: Bruno become friends with Sparky!

print(dog_one)
# This Golden Retriever named Sparky is 6 years old and has 1 friend/s. Sparky is friendly dog.
print(dog_two)
# This Chihuahua named Bruno is 10 years old and has 1 friend/s. Bruno is an unfriendly dog.

print("----------------------------------")
# Practise 02
print("Practise #02")

class HoldsFive:
  five = 5
  
five_holder = HoldsFive()
 
print(hasattr(five_holder, 'five')) # True

print("----------------------------------")
# Practise 03
print("Practise #03")

class User:
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return "Hiya {}!".format(self.name)
  
devorah = User("Devorah")
print(devorah) # Hiya Devorah!


print("----------------------------------")
# Practise 04
print("Practise #04")

# Create a python class called DriveBot. Within this class, create instance variables for motor_speed, sensor_range, and direction. All of these should be initialized to 0 by default. After setting up the class, create an object from the class called robot_1. Set the motor_speed to 5, the direction to 90, and the sensor_range to 10. Use the provided print statements to check your work!

class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0


robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)


print("----------------------------------")
# Practise 05
print("Practise #05")

# In the DriveBot class, add a method called control_bot which accepts parameters: new_speed and new_direction. These should replace the associated instance variables. Create another method called adjust_sensor which accepts a parameter called new_sensor_range which replaces the sensor_range instance variable. Afterwards, use these methods to rotate the robot 180 degrees at 10 miles per hour with a sensor range of 20 feet. Use the provided print statements to check your code!

class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0
    def control_bot(self, new_speed,  new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction    
 
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range   
    

robot_1 = DriveBot()
robot_1.motor_speed = 10
robot_1.direction = 180
robot_1.sensor_range = 20

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

print("----------------------------------")
# Practise 06
print("Practise #06")

# Upgrade the constructor in the DriveBot class in order to accept three optional parameters. The constructor can accept motor_speed (which defaults to 0 if not provided), direction (which defaults to 180 if not provided, and sensor_range (which defaults to 10 if not provided). These parameters should replace the associated instance variables. Test out the upgraded constructor by initializing a new robot called robot_2 with a speed of 35, a direction of 75, and a sensor range of 25.


class DriveBot:
  def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
    self.motor_speed = motor_speed
    self.direction = direction
    self.sensor_range = sensor_range


# sensor_range defaults to 10
test_bot_1 = DriveBot(10, 270) 
# direction defaults to 180
test_bot_2 = DriveBot(sensor_range = 20, motor_speed = 45) 
# direction defaults to 180 and sensor_range defaults to 10
test_bot_3 = DriveBot(50) 
# all default values are used
test_bot_4 = DriveBot() 
# no default values are used
test_bot_5 = DriveBot(18, 95, 30)    

robot_2 = DriveBot()
robot_2.motor_speed = 35
robot_2.direction = 75
robot_2.sensor_range = 25

print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

print("----------------------------------")
# Practise 07
print("Practise #07")

# Create a class variable called all_disabled which is set to False. Next, create two more class variables called latitude and longitude. Set both of those variables to equal -999999. A third robot has been created below the first two robots. Set the latitude of all of the robots to -50.0 at once. Additionally, set the longitude of the robots to 50.0 and set all_disabled to True. You should be able to set those values using three lines of code.

class DriveBot:
  # Create the class variables!
    all_disabled = False
    latitude = -999999
    longitude = -999999

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# Change the latitude, longitude, and all_disabled values for all three robots using only three lines of code!

DriveBot.longitude = 50.0
DriveBot.latitude = -50.0
DriveBot.all_disabled = True

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)

print("----------------------------------")
# Practise 08
print("Practise #08")

# Within the DriveBot class, create an instance variable called id which will be assigned to the robot when the object is created. Every time a robot is created, increment a counter (stored as a class variable) so that the next robot will have a different id. For example, if three robots were created: first_robot, next_robot, and last_robot; first_robot will have an id of 1 next_robot will have an id of 2 and last_robot will have an id of 3.

class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0
 
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count
 
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
 
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)

print("----------------------------------")
# Practise 09
print("Practise #09")
# [Pokemon Game through OOP from CodeAcademy]
# just copied and paste I have to come here again for better understanding and see how things works [02/28/2022]

class Pokemon:
    # To create a pokemon, give it a name, type, and level. Its max health is determined by its level. Its starting health is its max health and it is not knocked out when it starts.
    def __init__(self, name, type, level = 5):
        self.name = name
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.type = type
        self.is_knocked_out = False


    def __repr__(self):
        # Printing a pokemon will tell you its name, its type, its level and how much health it has remaining
        return "This level {level} {name} has {health} hit points remaining. They are a {type} type Pokemon".format(level = self.level, name = self.name, health=self.health, type = self.type)

    def revive(self):
        # Reviving a pokemon will flip it's status to False
        self.is_knocked_out = False
        # A revived pokemon can't have 0 health. This is a safety precaution. revive() should only be called if the pokemon was given some health, but if it somehow has no health, its health gets set to 1.
        if self.health == 0:
            self.health = 1
        print("{name} was revived!".format(name = self.name))

    def knock_out(self):
        # Knocking out a pokemon will flip its status to True.
        self.is_knocked_out = True
        # A knocked out pokemon can't have any health. This is a safety precaution. knock_out() should only be called if heath was set to 0, but if somehow the pokemon had health left, it gets set to 0.
        if self.health != 0:
            self.health = 0
        print("{name} was knocked out!".format(name = self.name))

    def lose_health(self, amount):
        # Deducts heath from a pokemon and prints the current health reamining
        self.health -= amount
        if self.health <= 0:
            #Makes sure the health doesn't become negative. Knocks out the pokemon.
            self.health = 0
            self.knock_out()
        else:
            print("{name} now has {health} health.".format(name = self.name, health = self.health))

    def gain_health(self, amount):
        # Adds to a pokemon's heath
        # If a pokemon goes from 0 heath, then revive it
        if self.health == 0:
            self.revive()
        self.health += amount
        # Makes sure the heath does not go over the max health
        if self.health >= self.max_health:
            self.health = self.max_health
        print("{name} now has {health} health.".format(name = self.name, health = self.health))

    def attack(self, other_pokemon):
        # Checks to make sure the pokemon isn't knocked out
        if self.is_knocked_out:
            print("{name} can't attack because it is knocked out!".format(name = self.name))
            return
        # If the pokemon attacking has a disadvantage, then it deals damage equal to half its level to the other pokemon
        if (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Grass" and other_pokemon.type == "Fire"):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = round(self.level * 0.5)))
            print("It's not very effective")
            other_pokemon.lose_health(round(self.level * 0.5))
        # If the pokemon attacking has neither advantage or disadvantage, then it deals damage equal to its level to the other pokemon
        if (self.type == other_pokemon.type):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level))
            other_pokemon.lose_health(self.level)
        # If the pokemon attacking has advantage, then it deals damage equal to double its level to the other pokemon
        if (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level * 2))
            print("It's super effective")
            other_pokemon.lose_health(self.level * 2)

class Trainer:
    # A trainer has a list of pokemon, a number of potions and a name. When the trainer gets created, the first pokemon in their list of pokemons is the active pokemon (number 0)
    def __init__(self, pokemon_list, num_potions, name):
        self.pokemons = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0
        self.name = name

    def __repr__(self):
        # Prints the name of the trainer, the pokemon they currently have, and the current active pokemon.
        print("The trainer {name} has the following pokemon".format(name = self.name))
        for pokemon in self.pokemons:
            print(pokemon)
        return "The current active pokemon is {name}".format(name = self.pokemons[self.current_pokemon].name)

    def switch_active_pokemon(self, new_active):
        # Switches the active pokemon to the number given as a parameter
        # First checks to see the number is valid (between 0 and the length of the list)
        if new_active < len(self.pokemons) and new_active >= 0:
            # You can't switch to a pokemon that is knocked out
            if self.pokemons[new_active].is_knocked_out:
                print("{name} is knocked out. You can't make it your active pokemon".format(name = self.pokemons[new_active].name))
            # You can't switch to your current pokemon
            elif new_active == self.current_pokemon:
                print("{name} is already your active pokemon".format(name = self.pokemons[new_active].name))
            # Switches the pokemon
            else:
                self.current_pokemon = new_active
                print("Go {name}, it's your turn!".format(name = self.pokemons[self.current_pokemon].name))

    def use_potion(self):
        # Uses a potion on the active pokemon, assuming you have at least one potion.
        if self.potions > 0:
            print("You used a potion on {name}.".format(name = self.pokemons[self.current_pokemon].name))
            # A potion restores 20 health
            self.pokemons[self.current_pokemon].gain_health(20)
            self.potions -= 1
        else:
            print("You don't have any more potions")

    def attack_other_trainer(self, other_trainer):
        # Your current pokemon attacks the other trainer's current pokemon
        my_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(their_pokemon)

# Six pokemon are made with different levels. (If no level is given, it is level 5)
a = Pokemon("Charmander", "Fire", 7)
b = Pokemon("Squirtle", "Water")
c = Pokemon("Lapras", "Water", 9)
d = Pokemon("Bulbasaur", "Grass", 10)
e = Pokemon("Vulpix", "Fire")
f = Pokemon("Staryu", "Water", 4)


#Getting input to get the trainers names and letting them select the Pokemon they want.
trainer_one_name = input("Welcome to the world of Pokemon. Please enter a name for player one and hit enter. ")
trainer_two_name = input("Hi, " + str(trainer_one_name) + "! Welcome! Let's find you an opponent. Enter a name for the second player. ")

choice = input("Hi, " + trainer_two_name + "! Let's pick our Pokemon! " + trainer_one_name + ", would you like a Level 7 Charmander, or a Level 7 Squirtle? " + trainer_two_name + " will get the other one. Type either 'Charmander' or 'Squirtle'. ")

while choice != 'Charmander' and choice != 'Squirtle':
  choice = input("Whoops, it looks like you didn't choose 'Charmander' or 'Squirtle'. Try selecting one again! ")

# Keeping track of which pokemon they chose
trainer_one_pokemon = []
trainer_two_pokemon = []

if choice == 'Charmander':
  trainer_one_pokemon.append(a)
  trainer_two_pokemon.append(b)

else:
  trainer_one_pokemon.append(b)
  trainer_two_pokemon.append(a)

# Selecting the second pokemon
choice = input(trainer_two_name + ", would you like a Level 9 Lapras, or a Level 10 Bulbasaur? " + trainer_one_name + " will get the other one. Type either 'Lapras' or 'Bulbasaur'. ")

while choice != 'Lapras' and choice != 'Bulbasaur':
  choice = input("Whoops, it looks like you didn't choose 'Lapras' or 'Bulbasaur'. Try selecting one again! ")

if choice == 'Lapras':
  trainer_one_pokemon.append(d)
  trainer_two_pokemon.append(c)

else:
  trainer_one_pokemon.append(c)
  trainer_two_pokemon.append(d)

# Selecting the third pokemon
choice = input(trainer_one_name + ", would you like a Level 5 Vulpix, or a Level 4 Staryu? " + trainer_two_name + " will get the other one. Type either 'Vulpix' or 'Staryu'. ")

while choice != 'Vulpix' and choice != 'Staryu':
  choice = input("Whoops, it looks like you didn't choose 'Vulpix' or 'Staryu'. Try selecting one again! ")

if choice == 'Vulpix':
  trainer_one_pokemon.append(e)
  trainer_two_pokemon.append(f)

else:
  trainer_one_pokemon.append(f)
  trainer_two_pokemon.append(e)
  
# Creating the Trainer objects with the given names and pokemon lists
trainer_one = Trainer(trainer_one_pokemon, 3, trainer_one_name)
trainer_two = Trainer(trainer_two_pokemon, 3, trainer_two_name)

print("Let's get ready to fight! Here are our two trainers")

print(trainer_one)
print(trainer_two)

# Testing attacking, giving potions, and switching pokemon. This could be built out more to ask for input
trainer_one.attack_other_trainer(trainer_two)
trainer_two.attack_other_trainer(trainer_one)
trainer_two.use_potion()
trainer_one.attack_other_trainer(trainer_two)
trainer_two.switch_active_pokemon(0)
trainer_two.switch_active_pokemon(1)
