class Loan:
    def __init__(self, annualInterestRate = 2.5, numberOfYears= 1,
                 loanAmount = 1000, borrower= ""):
        self.__anualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount
        self.__borrower = borrower


    def getAnnualInterestRate(self):
        return self.__anualInterestRate
    def getNumberOfYear(self):
        return self.__numberOfYears
    def getLoanAmount(self):
        return self.__loanAmount
    def getBorrower(self):
        return self.__borrower

    def setAnnualInterestRate(self, annualInterestRate):
        self.__anualInterestRate = annualInterestRate
    def setNumberOfYear(self, numberOfYear):
        self.__numberOfYears = numberOfYear
    def setLoanAmount(self, loanAmount):
        self.__loanAmount = loanAmount
    def setBorrower(self, borrower):
        self.__borrower = borrower

    def getMonthlyPayment(self):
        monthlyInterestRate = self.__anualInterestRate / 1200
        monthlyPayment = \
            self.__loanAmount * monthlyInterestRate / (1 - (1 /
                    (1 + monthlyInterestRate) ** (self.__numberOfYears * 12)))
        return monthlyPayment

    def getTotalPayment(self):
        toralPayment = self.getMonthlyPayment() * self.__numberOfYears * 12
        return toralPayment