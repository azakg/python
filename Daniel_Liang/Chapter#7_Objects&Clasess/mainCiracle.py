from Circle import Circle

def main():

    c1 = Circle(5)
    print(c1.getArea())
    print(c1.getPerimeter())
    print(c1.getRadius())
    c1.setRadius(10)
    print(f"This is after changin radius is : {c1.getRadius()}")

main()