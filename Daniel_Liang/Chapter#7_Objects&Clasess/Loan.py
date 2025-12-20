class Loan:
    def __init__(self,
               annualInterestRate = 2.5,
               numberOfYear = 1,
               loanAmount = 1000,
               borrower = " "):
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYear = numberOfYear
        self.__loanAmount = loanAmount
        self.__borrower = borrower

    def getMothlyPayment(self):
        monthlyInterestrate = self.__annualInterestRate/1200
        monthlyPayment = (
                self.__loanAmount * monthlyInterestrate /
                (1 - (1/(1+monthlyInterestrate)**(self.__numberOfYear * 12))))
        return monthlyPayment

