class Test:

    def __init__(self, name, color):

        self.name = name
        self.color = color

    def call_name(self):
        print(f"my name is {self.name.title()}")

    def favorite_color(self):
        print(f"My favorite color is {self.color}")


person = Test('azamat', 'green')
person.call_name()
person.favorite_color()
