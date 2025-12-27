class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getName(self):
        return self.__name
    def getSymbol(self):
        return self.__symbol

    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice
    def setPreviousClosingPrice(self, p):
        self.__previousClosingPrice = p

    def getCurrentPrice(self):
        return self.__currentPrice
    def setCurrentPrice(self, c):
        self.__currentPrice = c

    def getChangePercent(self):
        result = "%.2f" % (self.__currentPrice/(self.__previousClosingPrice / 100)-100)
        return f"{result}%"
