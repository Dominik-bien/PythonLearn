def greet_user():
    """Display simple greetings"""
    print("Hello!")

greet_user()

def greet_user(username):
    print(f"Hello, {username}")

greet_user('Dominik')

def display_messages():
    print("In this lesson I learn use functions in Python")

display_messages()

def favourite_book(book): 
    print(f"Your favourite book: {book}")

favourite_book('The Wheel of time - Robert Jordan')

##

def describe_pet(animal_type, pet_name): 
    print(f"My pet is: {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('dog', 'lola')
describe_pet('cat', 'kinia')
describe_pet(animal_type='parrot', pet_name='Kiwi')

def describe_pet(pet_name, animal_type='dog'):
    print(f"My pet is {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")

describe_pet(pet_name="Willie")
describe_pet(pet_name="willie")

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

def make_shirt(size, title):
    print(f"T-Shirt size: {size}")
    print(f"Inscription on T-Shirt: {title} ")

make_shirt(42, 'I love this')

## 
def make_shirt(size='huge', title='I love Python'): 
    print(f"T-shirt size: {size}")
    print(f"Inscription on T-Shirt: {title}")

make_shirt()
make_shirt('medium', 'I like cakes')
make_shirt('Little', 'Math is my passion')

##
def describe_city(city, country='Poland'):
    print(f"City: {city}")
    print(f"This city is places on {country}")

describe_city('Krakow')
describe_city('Warsaw', 'Poland')
describe_city('Eindhoven', 'Nederland')
describe_city('Berlin', 'Germany')

# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# def get_formatted_name(first_name, middle_name, last_name):
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()



# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)


def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person 

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

##

# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("Enter your name and surname please: ")
#     print("If you want exit to the program enter q")
#     name = input("Name: ")
#     if name == 'q': 
#         break 

#     surname = input("Surname: ")
#     if surname == 'q':
#         break

#     formatted_name = get_formatted_name(name, surname)
#     print(f"\nHi, {formatted_name}")

def city_country(city, country):
    location = f"{city}, {country}"
    return location.title()

my_city = city_country('Krakow', 'Poland')
print(my_city)
kamil_city = city_country('Eindhoven', 'Nederland')
print(kamil_city)
kacper_city = city_country('Tokyo', 'Japan')
print(kacper_city)

# def make_album(title, team_name):
#     band = {'Team': team_name.title(), 'Album Title': title.title()}
#     return band

# band1 = make_album('The last stand', 'sabaton') 
# print(band1)
# band2 = make_album('Call of the wind', 'Powerwolf')
# print(band2)
# band3 = make_album('Abbey road', 'The beatles')
# print(band3)

# while True: 
#     print("Enter title for album: ")
#     print("If you want quit the program press 'q' ")
#     title_album = input('Title: ')
#     if title_album == 'q': 
#         break

#     band_name = input("Band: ")
#     if band_name == 'q': 
#         break

#     formatted_name = make_album(title_album, band_name)
#     print(formatted_name)

    ## 
def greet_users(names): 
        for name in names: 
            msg = f"Hello, {name.title()}!"
            print(msg)

usernames = ['halina', 'tymek', 'marzena']
greet_users(usernames)

unprinted_designs = ['etui', 'robot', 'pentagon']
completed_models = []

while unprinted_designs: 
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nPrinted models: ")
for completed_model in completed_models:
    print(completed_model)






def print_models(unprinted_designs, completed_models):
    while unprinted_designs: 
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("Printed models: ")
    for completed_model in completed_models: 
        print(completed_model)

unprinted_designs = ['etui', 'figure', 'robot', 'pentagram']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print_models(unprinted_designs[:], completed_models)

def show_messages(messages):
    for message in messages:
        print(message)

msg = ['I love cakes', 'My puupy is annoying', 'Python is Fun', 'I want create games']
show_messages(msg)

def send_messages(msg, complete_show):
    while msg: 
        print("I send message")
        current_msg = msg.pop()
        complete_show.append(current_msg)
    

def show_messages(send_messages): 
    print("I print request messages: ") 
    for message in send_messages: 
        print(message)


msg = ['I love cakes', 'My pizza is tasty']
complete_show = []

send_messages(msg, complete_show)
show_messages(complete_show)

##

def make_pizza(*toppings): 
    print(toppings)

make_pizza('pepperoni')
make_pizza('Mushroons', 'extra cheese', 'green pepper')


def make_pizza(*toppings):
    print("\nI prepar pizza with following toppings: ")
    for topping in toppings: 
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('Mushroons', 'green pepper', 'extra cheese')

def make_pizza(size, *toppings):
    print(f"\n I prepare pizza with {size} size cm with following toppings: ")
    for topping in toppings: 
        print(f"- {topping}")

make_pizza(40, 'pepperoni')
make_pizza(30, 'mushroons', 'green pepper', 'extra Cheese')

def build_profile(first, last, **user_info):
    user_info['first_name'] = first 
    user_info['last_name'] = last
    return user_info 

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

def sandwitch_maker(*ingrements): 
    print("I create sandwitch with following ingrements: ")
    print("---------------")
    for ingrement in ingrements: 
        print(f"- {ingrement}")

    print("---------------")

sandwitch_maker('ham')
sandwitch_maker('cheese', 'ham')
sandwitch_maker('cheese', 'ham', 'pinkle')


def build_profile(first, last, **user_info): 
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('Dominik', 'Bien',
                           location='Zalas',
                           field = 'Programming',
                           hobby = 'Create games, programming, reading books, playing the organ')
print(my_profile)


def make_car(name, model, **car_info): 
    car_info['Name'] = name
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='grey', tow_package=True)
print(car)