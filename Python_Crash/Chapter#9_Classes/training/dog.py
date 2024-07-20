class Dog:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} is rolling over")

    def info(self):
        print(f"Name of the dog is {self.name}\nAge of the dog is {self.age}")


my_dog = Dog('Alpha', 3)
my_dog.sit()
my_dog.roll_over()
my_dog.info()

