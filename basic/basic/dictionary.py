alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You gained {new_points} points!")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0 ['color'] = 'yellow'
alien_0 ['points'] = 5

print(alien_0)
print(f"alien has got {alien_0['color']} color")
alien_0['color'] = 'red'
print(f"alien has got {alien_0['color']} color")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Inital value for x_position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] +  x_increment
print(f"New x_position value: {alien_0['x_position']}")

##
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

favourite_languages = {
    'Dominik': 'c#',
    'Kacper': 'c',
    'Bartosz': 'python',
    'Kamil': 'c++'
}

language = favourite_languages['Kacper'].title()
print(f"Favourite programming languages Kacper is: {language}")

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No assigned points')
print(point_value)

person = {'First Name': 'Fryderyk', 'Last Name': 'Chopin', 'age': 30, 'city': 'Zelazna Wola'}
print(person) 

favourite_numbers = {'Kacper': 21, 'Dominik': 7, 'Kamil': 69, 'Maciek': 32, 'Tom': 3}
print(favourite_numbers) 

words = {'If' : 'conditional instruction', 'for': 'loop', 'int': 'data types',
         'print': 'displays the value in terminal'}


for key, value in words.items(): 
    print(f'{key}, definiction: {value}')
    print('\n')

user_0 = {
    'username': 'jkowalski',
    'first': 'jan',
    'last': 'kowalski'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")

favourite_languages = {
    'pawel': 'c#',
    'sara': 'c',
    'edward': 'python',
    'janek': 'c++'
}

for name, language in favourite_languages.items():
    print(f"Favourite programming language user {name.title()} is: {language.title()}")

for name in favourite_languages.keys():
    print(name.title())

friends = ['pawel', 'sara']
for name in favourite_languages.keys(): 
    print(f"Hi", {name.title()})

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\tHi, {name.title()} ", 
              "! I see that your favourite programming language is {language}!")
    if 'elzbieta' not in favourite_languages.keys():
        print("Elzbieta pls take part in the survey")    
    
    favourite_languages = {
    'pawel': 'c#',
    'sara': 'c',
    'edward': 'python',
    'janek': 'c++'
}
    for name in sorted(favourite_languages.keys()):
        print(f"{name.title()}, thank you for take part in the survey")


print("the following programming languages are listed in the survey:")
for language in favourite_languages.values():
    print(language.title())

for key, value in words.items(): 
  print(f'{key}, definiction: {value}')
  print('\n')

rivers = {'Wisla': "Poland", 'Nil': 'Egypt', 'Rhine': "Nederlands"}
for river, country in rivers.items(): 
    print(f"{river.title()} flows through: {country.title()}")
for river in rivers.keys(): 
    print(river.title())
for country in rivers.values():
    print(country.title())


##
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alient_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alient_2]
for alien in aliens: 
    print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]: 
    print(alien)
print("...")

print(f"Integer aliens amount: {len(aliens)}")

aliens = []

for alien_number in range (30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

##
pizza = {
    'Crust': 'PAN',
    #list 
    'toppings': ['Mushroons', 'Extra Cheese']
}
print(f"You order pizza on {pizza['Crust']} dough" 
      "with the following ingrements: ")

for topping in pizza['toppings']:
    print(f"\t{topping}")

favourite_languages = {
    'pawel': 'C',
    'sara': ['C#', 'Assembler'],
    'edward': ['python', 'Go'],
    'janek': ['C++', 'Rust' ]
}

for name, languages in favourite_languages.items(): 
    print(f"\nFavourite programming language user {name.title()} are: ")
    for language in languages: 
        print(f"\t{language.title()}")

##
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'Maria',
        'last': 'sklodowska-curie',
        'location': 'Paris',
    },

}

for username, user_info in users.items(): 
    print(f"\n Username: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFirst and Last name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


person = {'First Name': 'Fryderyk', 'Last Name': 'Chopin', 'age': 30, 'city': 'Zelazna Wola'}
print(person) 

people = {
    'Person1': {
        'Name': 'fryderyk',
        'Surname': 'Chopin',
        'Location': 'Zelazna-wola',
    },
    'Person2': {
        'Name': 'Grzegorz',
        'Surname': 'Niemczuk',
        'Location': 'Bielsko-biala',
    },
    'Person3': {
        'Name': 'Kacper',
        'Surname': 'Lelito', 
        'Location': 'Krakow',
    },

}

for person, person_info in people.items(): 
    print(f"Person: {person}")
    full_name = f"{person_info['Name']} {person_info['Surname']}"
    location = person_info['Location']

    print(f"\tName and Surname: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
