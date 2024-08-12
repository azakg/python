from Circle import Circle

def main():

    myCircle = Circle()

    n = 5
    printAreas(myCircle, n)

def printAreas(c, times):

    print("Radius \t\tArea")
    while times >= 1:
        print(c.radius, "\t\t|\t", c.getArea())
        c.radius = c.radius + 1
        times = times - 1

main()