from Circle import Circle, Circle1

def main():
    circle1 = Circle()
    print("The area of the circle of radius ", circle1.radius, " is ", circle1.getArea())

    circle2 = Circle(25)
    print("Ther area of the circle of radius ", circle2.radius, " is ", circle2.getArea())

    circle3 = Circle(125)
    print("The area of the circle of radius ", circle3.radius, " is ", circle3.getArea())

    #Modify circle radius
    circle2.radius = 100

    print("The area of the circle of radius", circle2.radius, " is ", circle2.getArea())

    circle1.radius = 200
    circle1.color = "white"
    print("The Circle1 radius is: ", circle1.radius)
    print("Color of the Circle1 is: ", circle1.color)



    list1 = [1, 3, 6, 8, 9]
    print(max(list1))


main()