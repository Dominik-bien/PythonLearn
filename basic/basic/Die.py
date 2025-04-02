import random 
class Die:
    def __init__(self, sides = 6):
        self.sides = sides 

    def roll_die(self):
        roll = random.randint(1, self.sides)
        print(f"Retrieved: {roll}")
        

my_die = Die()
my_die.roll_die()

my_die2 = Die(10)
my_die2.roll_die()

my_die3 = Die(20)
my_die3.roll_die()