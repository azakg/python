class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def getBMI(self):
        KG_PER_POUND = 0.45359237
        M_PER_INCH = 0.0254
        bmi = self.__weight * KG_PER_POUND / ((self.__height * M_PER_INCH) * (self.__height * M_PER_INCH))
        return round(bmi * 100)/100
    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 20:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
