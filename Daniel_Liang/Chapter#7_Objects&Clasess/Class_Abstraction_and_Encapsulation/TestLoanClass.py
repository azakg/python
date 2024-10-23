from Loan import Loan

def main():
    annualInterestRate = eval(input("Enter yearly interest rate, for example, 7.25: "))

    numberOfYear = eval(input("Enter number of years as an integer: "))

    loanAmount = eval(input("Enter loan amount, for example, 120000.95: "))

    borrower = input("Enter a borrower's name: ")

    loan = Loan(annualInterestRate, numberOfYear, loanAmount, borrower)

    print("The loan is for ", loan.getBorrower())
    print("The monthly payment is ", format(loan.getMonthlyPayment(), ".2f"))
    print("The total payment is ", format(loan.getTotalPayment(), ".2f"))

main()
