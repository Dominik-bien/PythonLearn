bicycles = ['mountain', 'trekking', 'city', 'road']
print(bicycles)
print(bicycles[0].title())
message = f"My first bicycle is : {bicycles[1].title()} bicycle."
print(message)

names = ['Daniel', 'Kacper', 'Marzenka', 'Piotr']
message1 = "Hi"
print(message1, names[0].title())
print(message1, names[1].title())
print(message1, names[2].title())
print(message1, names[3].title())

favourite_vehicle = ['car', 'bike', 'plane', 'train', 'scooter']
model = ['xiaomi', 'Jaguar', 'BMW', 'Toyota']
print(f"I want to have: {model[0].title()}, {favourite_vehicle[0].title()}")
print(f"I want to have: {model[1].title()}, {favourite_vehicle[2].title()}")
print(f"I want to have: {model[3].title()}, {favourite_vehicle[1].title()}")

favourite_vehicle.append('Bus'); 
print(favourite_vehicle)
model.insert(1, 'Suzuki')
print(model)
del model[3]
print(model)
model.remove('Jaguar')
print(model)
## 

guests = ['Daniel', 'Marzenka', 'Chopin', 'Bach']
leave_guest = 'Chopin' 
guests.remove(leave_guest)
print(f'Guest {leave_guest} can not come because he has played concert')
guests.append('Mario')
print(f'Guest: {guests[-1]} can arrive because he loves spaghetti')
guests.insert(0, 'Nicolaj')
guests.insert(3, 'Alcest')
guests.append('Kleofas')
print(len(guests))
message2 = f'Welcome to my dinner Today {guests}'
print(message2)
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
message3 = f'Today I have only dinner for 2 guests: {guests}'
print(message3)
del guests[0]
del guests[0]
print(guests)
##
cars = ['bmv', 'audi', 'mercedes', 'subaru', 'honda']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
print(f'Inital list: {cars}')
cars = ['bmv', 'audi', 'mercedes', 'subaru', 'honda']
[print(cars)]
cars.reverse()
print(cars)
print(len(cars))

cities = ['Eindhoven', 'Amsterdam', 'Kopenhaga', 'Oslo', 'Reykjavík']

print(sorted(cities))

print(cities)

sorted_city = sorted(cities, reverse = True)
print(sorted_city)
print(cities)
print(cities.reverse())
print(cities.reverse())
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)
