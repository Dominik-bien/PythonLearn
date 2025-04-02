cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars: 
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = "muschroons"

if requested_topping != 'anchois':
    print("One anchois please!")


##
answer = 17
if answer != 42:
    print("Its not correct answer. Try again!")

banned_users = ['andrzej', 'stefan', 'dominik', 'dawid']
user = 'maria'

if user not in banned_users: 
    print(f"{user.title()}, you can publish answer, if you want")

    car = 'Toyota'

    if car == 'subaru':
        print("I predict true.")
        print(car == 'subaru')
    else:  
        print("I predict false")
        print(car == 'audi')


pasta = 'spaghetti'
if pasta != 'carbonara':
    print("I want carbonara")

games = ["The witcher", "Skyrim", "World of warcraft", 'League']
my_game = "Morrowind"

if not my_game in games: 
    print(f"I should play {my_game}")
else:
    print(f"I don't want play this game")


##

age = 12
if age < 4: 
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 20
else:
    price = 40

print(f"Ticket cost: {price} dollars")

requested_topping = ['muschroons', 'extra cheese']

if 'muschroons' in requested_topping: 
    print("add muschroons")
if 'extra cheese' in requested_topping: 
    print("add extra cheese")

print("\nYour pizza is ready")

alien_color = ['green', 'yellow', 'blue']
points = 0

if 'green' in alien_color:
     print("You gained 5 points")
     points += 5
elif 'blue' in alien_color:
    print("you gained 10 points")
    points += 10
elif 'yellow' in alien_color: 
    print("you gave 15 points")
    points += 15
else: 
    print("You don't gave any points")

## 
age = 15
if age < 2: 
    print("You are baby")
elif age >= 2 and age < 4:
    print("You are baby which learn walk")
elif age >= 4 and age < 13: 
    print("You are child")
elif age >= 13 and age < 20:
    print("You are teenager")
elif age >= 20 and age < 65:
    print("You are adult")
else:
    print("You are senior")

##
favourite_fruits = ['banana', 'peach', 'strawberry', 'blackberry', 'rasberry']

if 'banana' in favourite_fruits: 
    print(f"You are really love banana")
if 'peach' in favourite_fruits: 
    print(f"You are really love peach")
if 'strawberry' in favourite_fruits: 
    print(f"You are really love strawberry")
if 'blackberry' in favourite_fruits: 
    print(f"You are really love blackberry")
if 'rasberry' in favourite_fruits: 
    print(f"You are really love rasberry")
        
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Add {requested_topping}.")
    print("\n Your pizza is ready!")
else:
    print("Do you want pizza without toppings?")


available_toppings = ['Mushroons', 'olive', 'bacon', 
                      'pepperoni', 'ananas', 'extra cheese']
requested_toppings = ['Mushroons', 'fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Add {requested_topping}")
    else:
        print(f"Sorry. We haven't this topping: {requested_topping}")
print("\nYour pizza is ready!")

users = ['Dominik', 'admin', 'nikolaj', 'tom', 'stanley']


for user in users: 
    if user == 'admin':
        print(f"Welcome {user}! Do you want review today's report?")
    else:
        print(f"Welcome, {user}! Thank you for one login again")


users = []
if users:
    for user in users:
         print(f"Welcome, {user}! Thank you for one login again")
else:
    print("We have to find some users")

##
current_users =  ['Dominik', 'Kacper', 'Nikolaj', 'Tom', 'Stanley']
new_users = ['Dominik', "Bill", 'Eva', 'nikolaj', 'Dipper', "Mabbel"]
current_users1 = ['dominik', 'kacper', 'nikolaj', 'tom', 'stanley']


for new_user in new_users:
    if new_user in current_users and new_user in current_users1:
        print(f"We have this {new_user} name on our database. Enter another name")
    else:
        print(f"You can use this {new_user} on our database.")

##
for i in range(1, 10):
    if i == 1:
        print(f"{i}th")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")
        

