from car import Car
import electric_car as ec


my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ec.ElectricCar('nissan', 'lead', 2024)
print(my_leaf.get_descriptive_name())

"""my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()"""