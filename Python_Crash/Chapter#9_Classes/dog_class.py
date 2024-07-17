class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")



my_dog = Dog('Alfa', 6)
my_dog.sit()
my_dog.roll_over()

my_sec_dog = Dog('Lucy', 3)
my_sec_dog.sit()
my_sec_dog.roll_over()

print(f"My dog's name is {my_dog.name}")
