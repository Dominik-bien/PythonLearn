magicians = ['alicja', 'dawid', 'karolina']
for magician in magicians:
    print(f"{magician.title()}, it was awesome trick")
    print(f"I can't wait to ext trick {magician.title()}\n")

    print("Thank everything. It was really excellent show")


pizzas = ['Cappriciosa', 'Margherita', 'Greek', 'Pepperoni']
for pizza in pizzas: 
    print(f"I love {pizza}")

print("I really love pizzas")

animals = ['Cat', 'Dog', 'Horse']
for animal in animals: 
    print(f"{animal} is real human's firend")

print("All mentioned animals are awesome")

##
for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)

for value in range(1, 21):
    print(value)

##for value in range(1, 1000001):
  ##  print(value)

# squares = []
# for value in range(1, 1000001):
#     squares.append(value)

# print(squares)
# print(min(squares))
# print(max(squares))
# print(sum(squares))

for value in range(1, 21, 2):
    print(value)

Third = [value**3 for value in range(3, 31)]
print(Third)

Thirds = []
for value in range(1, 11):
    third = value ** 3
    Thirds.append(third)
print(Thirds)

Thirds = [value**3 for value in range(1, 11)]
print(Thirds)

players = ['karol', 'martyna', 'michal', 'florian', 'ela', "marcin"]
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print("Here are 3 first Players our Team: ")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'spaghetti', 'sandwich', 'Carrot Cake']
friend_foods = my_foods[:]

print("My favourite foods: ")
print(my_foods)

print("Favourite food my friend: ")
print(friend_foods)

my_foods.append("Cheese")
friend_foods.append("Apple")
print(my_foods)
print(friend_foods)

for player in players[:3]:
    print(f"First three element in this list: {player}")

print(f"Centre element in this list: {players[3:]}")

print(f"Last 3 element in this list: {players[-3:]}")


my_pizza = ['Cappriciosa', 'Margherita', 'Greek', 'Pepperoni']
your_pizza = my_pizza[:]

my_pizza.insert(0, "Diablo")
your_pizza.append("Haway")

print("My favourite pizzas: ")
for pizza in my_pizza:
    print(pizza)

print("Your favourite pizza: ")
for pizza in your_pizza: 
    print(pizza)


for food in my_foods: 
    print(food)

for food in friend_foods: 
    print(food)

##    

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions: 
    print(dimension)

print("Initial Dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Dimension after changing: ")
for dimension in dimensions:
    print(dimension)

buffets = ("Tomato Soup", "Spaghetti", "Fish and French fries", "pork chop with potatos", "salad")
for buffet in buffets: 
    print(buffet)


buffets = ("Tomato Soup", "Spaghetti", "Pizza", "hamburger", "salad")
for buffet in buffets:
    print(buffet)