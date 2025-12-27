from Rectangle import Rectangle

def main():
   w = eval(input("Please type width: "))
   h = eval(input("Please type hight: "))

   rectanlge1 = Rectangle(w, h)
   print(f"Area is: {rectanlge1.getArea()}")
   print(f"Perimeters is: {rectanlge1.getPerimeter()}")

main()