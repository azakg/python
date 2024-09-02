def add(*args):
   for n in args:
      print(type(n))

list = [1,2,3,4,5,6]
tuple_list = (2,3,4,5,6)
dic_list = {1:2, 2:3, 3:4}

add(list, tuple_list, dic_list)


#______________________________________________________________
def add1(*args):
   sum = 0
   for n in args:
      sum += n
   return sum

print(add1(1,2,3,4,5,6,7))

#______________________________________________________________

def add2(*args):
   for n in args:
      print(n)

a = [1,2,3]
b = [*a,4,5,6]
print(add2(b))

print("##########################")

#______________________________________________________________
def make_pizza(size, *toppings):
   print(f"\nMaking a {size} pizza with the following toppings: ")
   for n in toppings:
      print(n)

make_pizza(16, "onion", "mashroonm", "apple")

#______________________________________________________________

# def calculate(**kwargs):
#    print(kwargs)
#
#    for key,value in kwargs.items():
#       print(f"key is: {key}, and value is: {value}")
#
#
#
# calculate(add=3, multiply=5)

#______________________________________________________________

def calculator(ac, *kwargs):
   action = ac
   value_list = []
   for v1 in kwargs:
      value_list.append(v1)

   if action == "add":
      return value_list[0]+value_list[1]
   if action == "dev":
      return value_list[0]-value_list[1]


print(calculator("add", 1, 2))

#______________________________________________________________
def calculate(n, **kwargs):

   n += kwargs['add']
   n *= kwargs["multiply"]
   print(n)


calculate(2, add=3, multiply=5)


class Car:
   def __init__(self, **kw):
      # self.make = kw["make"]
      # self.model = kw["model"]
      self.make = kw.get("make")
      self.model = kw.get("model")

#my_car = Car(make="Toyota", model="Avalon")
my_car = Car(make="Toyota")
print(my_car.make)
print(my_car.model)