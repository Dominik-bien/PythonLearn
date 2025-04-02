class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self): 
        print(f"Restaurant name: {self.restaurant_name}.\nCuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is opened at: 12:00 P.M")

    def set_number_served(self, clients):
        if clients >= self.number_served:
            self.number_served = clients 
        else: 
            print("You cant assign new clients") 
    def print_served(self):
        print(f"Number client served: {self.number_served}")

    def increment_number_served(self, clients):
        self.number_served += clients 

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Strawberry', 'Vanilia', 'choclate', 'cookies', 'green apple']

    def available_flavours(self):
        print(f"Our Ice Screm {self.restaurant_name} Stand has available flavours: {self.flavors}")