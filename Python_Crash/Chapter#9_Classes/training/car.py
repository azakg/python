class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

class Electric_car(Car):

    def __init__(self, make, model, year, battery):
        super().__init__(make, model, year)

        self.battery = battery

    def read_odometer(self):
        print("This is electric car")


    def get_battery(self):
        print(f"Battery size is: {self.battery}")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_leaf = Electric_car("Nissan", "Leaf", "2025", 100)
print(my_leaf.get_descriptive_name())
my_leaf.get_battery()
my_leaf.read_odometer()