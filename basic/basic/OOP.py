class Dog:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    

    def sit(self):
        print(f"{self.name} is sitting now")
    
    def roll_over(self):
        print(f"{self.name} is laid back now")


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 5)
print(f"My dog is called: {my_dog.name.title()}")
print(f"My dog has {my_dog.age} years old.")
my_dog.sit()

print(f"Your dog is called: {your_dog.name.title()}")
print(f"Your dog has {your_dog.age} years old.")
your_dog.sit()

class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self): 
        print(f"Restaurant name: {self.restaurant_name}.\nCuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is opened at: 12:00 P.M")


restaurant1 = Restaurant("Frykas", "Polish cuisine")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

Restaurant2 = Restaurant('McDonalds', 'Fast Food')
Restaurant2.describe_restaurant()
Restaurant2.open_restaurant()

Restaurant3 = Restaurant('North Fish', "Fishes")
Restaurant3.describe_restaurant()
Restaurant3.open_restaurant()

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attepts = 0

    def describe_user(self):
        full_name = f"{self.first_name.title()} {self.last_name}"
        print(full_name)

    def greet_user(self):
        print(f"Hi! {self.first_name} {self.last_name}")

    def increment_login_attempts(self, attempts): 
        self.login_attepts += attempts

    def reset_login_attempts(self): 
        self.login_attepts = 0

    def print_login_attempts(self):
        print(f"Login attempts: {self.login_attepts}")

class Privileges: 
    def __init__(self, privileges=['Add post', 'Delete Post', 'Ban User']):
        self.privileges = privileges

    def show_privileges(self):
        
        print(f"Your privileges: {self.privileges}")

        

class Admin(User): 
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


   

first_admin = Admin("Kamil", "Nowak")
first_admin.privileges.show_privileges()
    
user1 = User("Dominik", "Bień")
user1.describe_user()
user1.greet_user()

user2 = User("Marzenka", "Ziabek")
user2.describe_user()
user2.greet_user()

user3 = User("Rand", "Al'thor")
user3.describe_user()
user3.greet_user()

user1.increment_login_attempts(10)
user1.print_login_attempts()
user1.reset_login_attempts()
user1.print_login_attempts()


##car




##restaurant





##aga = IceCreamStand("Aga", "Ice Creams")
##aga.available_flavours()

##
