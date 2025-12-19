from Circle import Circle

def main():
    myCircle = Circle()

    n = 5
    printArea(myCircle, n)


def printArea(c, times):
    print("radius \t\tArea")
    while times >= 1:
        print(f"{c.radius} \t\t\t{c.getArea()}")
        times -=1
        c.radius +=1

main()