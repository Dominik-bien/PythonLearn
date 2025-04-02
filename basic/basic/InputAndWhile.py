##message = input("Tell me something about yourself ")
#print(message)

#name = input("Enter your name: ")
#print(f"Hello, {name}!")

# prompt = "If tell us who are you we display message."
# prompt += "\nWhat's your name? "

# name = input(prompt)
# print(f"\nHello, {name}")

# height = input("How tall are you? (cm) ")
# height = int(height)

# if height >= 90:
#     print("\nYou are enough tall to ride")
# else:
#     print("\nYou will be able to ride if you grow up")

# number = input("Enter number: ")
# number = int(number)

# if number % 2 == 0: 
#     print("Even")
# else: 
#     print("Odd")

# cars = input("What make of car would you like to hire? ")
# print(f"One moment, I check if we have available {cars.title()} car")

# booking = int(input("How many tables you need: "))

# if booking > 8:
#     print("One moment, Please Wait to table")
# else: 
#     print("Your table is ready")

# number = int(input("Enter number: "))

# if number % 10 == 0: 
#     print("Your number is multiple of number 10")
# else: 
#     print("Your numer  isn't multiple of number 10")


# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1


# prompt = "If tell us who are you we display message."
# prompt += "\nWhat's your name? "
# message = ""
# while message != 'end': 
#     message = input(prompt)
    

#     if message != 'end':
#         print(message)



# prompt = "\nIf tell us who are you we display message."
# prompt += "\nEnter 'end' to exit the program. "

# active = True
# while active: 
#     message = input(prompt)

#     if message == 'end': 
#         active = False
#     else:
#         print(message)



# prompt = "\nEnter cities name, which you want to visit."
# prompt += "\nEnter 'end' to exit the program. "

# while True: 
#     city = input(prompt)

#     if city == 'end':
#         break
#     else:
#         print(f"I want visit {city.title()}!")

# current_number = 0
# while current_number < 10: 
#     current_number += 1 
#     if current_number % 2 == 0:
#         continue

#     print(current_number)


# pizza = "Enter ingrements to your pizza :D: "

# active = True

# while active == True: 
#     message = input(pizza)

#     if message == 'end':
#         break
#     else: 
#         print(f"Your ingrements for your pizza: {message}")


# message = "Enter your age: "
# message += "Enter -1 to exit program"

# while True: 
#     age = int(input(message))

#     if age == -1: 
#         break

#     if age < 3: 
#         print("Ticket for babies is free")
#     elif age >= 3 and age < 12:
#         print("Ticket cost 10 PLN")
#     elif age >= 12 and age < 15: 
#         print("Ticket cost 15 PLN") 
#     else: 
#         print("Ticket cost 20 PLN")

# unconfirmed_users = ['alicja', 'bartek', 'katarzyna']
# confirmed_users = []

# while unconfirmed_users: 
#     current_user = unconfirmed_users.pop()

#     print(f"Authentication user: {current_user.title()}")
#     confirmed_users.append(current_user)

#     print("\nThe listed user have been verificed: ")
#     for confirmed_user in confirmed_users:
#         print(confirmed_user.title())

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets: 
#     pets.remove('cat')

# print(pets)

# responses = {}
# polling_active = True 
# while polling_active:
#     name = input("\nWhat's your name? ")
#     response = input("Which peak do you want climb? ")

#     responses[name] = response

#     repeat = input('Does anyone else want to take part in survey? (yes/no)')
#     if repeat == 'no':
#         polling_active = False

# print("\n---Survey score---")
# for name, response in responses.items(): 
#     print(f"{name} wants climb to {response}.")


# sandwich_orders = ['Salami sandwich', 'Cheese sandwich', 'Salami sandwich', 'sandwich with vegetables', 
#                    'Jam sandwich', 'Salami sandwich']
# finished_sandwiches = []

# while sandwich_orders: 
#     current_sandwich = sandwich_orders.pop()
#     print(f"Ordered: Sandwich: {current_sandwich}")

#     finished_sandwiches.append(current_sandwich)

#     while 'Salami sandwich' in finished_sandwiches: 
#         finished_sandwiches.remove('Salami sandwich')

#     print("Our order status: ")
#     for sandwich in finished_sandwiches: 
#         print(sandwich.title())

responses = {}
polling_active = True
while polling_active: 
    name = input("Whats your name? ")
    response = input("Where do you want go on Holiday? ")

    responses[name] = response

    repeat = input("Do you want finished survey? (yes/no) ")
    if repeat == 'no':
        polling_active = False; 
    
print("Score")
for name, response in responses.items(): 
    print(f"{name} wants go to {response}")