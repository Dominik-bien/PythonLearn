class Car: 
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_raading = 0

    def  get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has travelled: {self.odometer_raading} km.")

    def update_odometer(self, mileage): 
        if mileage >= self.odometer_raading:
            self.odometer_raading = mileage
        else:
            print("cannot be reserved odometer")

    def increment_odometer(self, kilometers):
        self.odometer_raading += kilometers

class Battery: 
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car have acumulator by capacity: {self.battery_size} kWh")

    
    def upgrade_battery(self):
        if self.battery_size == 65: 
            print("Battery is already upgraded!")
        else: 
            self.battery_size = 65
            print(f"Upgraded the battery for this car to: {self.battery_size} kWh")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"Your car's range is about {range} km with a full battery.")



class ElectricCar(Car): 
    def __init__(self, make, model, year): 
        super().__init__(make, model, year)
        self.battery = Battery()



    def fill_gas_tank(self):
        print(f"This car not required fuelling")

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.fill_gas_tank()
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

# my_electric = ElectricCar('Fiat', 'Panda', 2023)
# my_electric.battery.get_range()
# my_electric.battery.upgrade_battery()
# my_electric.battery.get_range()