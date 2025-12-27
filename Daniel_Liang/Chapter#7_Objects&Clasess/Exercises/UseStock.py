from Stock import Stock

def main():
    Symbol = input("Please type symbol: ")
    Name = input("Please type name: ")
    CurrentPrice = eval(input("Please type current price: "))
    PreviousClosingPrice = eval(input("Please type previous price: "))
    stock1 = Stock(Symbol, Name, PreviousClosingPrice, CurrentPrice)
    print(stock1.getChangePercent())


main()