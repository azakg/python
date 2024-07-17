class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, time=''):
        self.rest_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open_time = time
    def describe_restaurant(self):
            print(f"Name of the restaurant is {self.rest_name}")
            print(f"Cuisine type is {self.cuisine_type}")
    def open_restaurant(self):
            print(f"Restaurant {self.rest_name} open time is {self.open_time}")

class User:
    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name

    def describe_user(self):
        print(f"User name is {self.f_name.title()}")
        print(f"User last name is {self.l_name.title()}")
    def greet_user(self):
        print(f"Hello {self.f_name.title()} {self.l_name.title()}")


italia = Restaurant('Villaggio', 'Italian', '9:00-18:00')
italia.describe_restaurant()
italia.open_restaurant()

first_user = User('azamat', 'apsamatov')
first_user.describe_user()
first_user.greet_user()

