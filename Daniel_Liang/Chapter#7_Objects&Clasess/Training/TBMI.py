class TBMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height =  height

    def getTBMI(self):
        KILOGRAMS_PER_POUND = 0.45359237
        METERS_PER_INCH = 0.0254

        tbmi = self.__weight * KILOGRAMS_PER_POUND / (2 * (self.__height * METERS_PER_INCH))
        return round(tbmi * 100)/100
    def getStatus(self):
        tbmi = self.getTBMI()
        if tbmi  < 18.5:
            return "Underweight"
        elif tbmi < 25:
            return "Normal"
        elif tbmi < 30:
            return "Overweight"
        else:
            return "Obese"