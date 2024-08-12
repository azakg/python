from Car import Car

def main():
    firstCar = Car()

    secondCar = Car('Black', 'SUV')

    print("First car color is ", firstCar.getColor())
    firstCar.setColor('yellow')
    print("We change color of first car, now it is ", firstCar.getColor())

    print("Second car's color is ", secondCar.getColor(), " and type is ", secondCar.getType())

main()