class Animal:

    def __init__(self):
        num_eye = 2

    def breath(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("doing this underwater")

    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.waterWings)