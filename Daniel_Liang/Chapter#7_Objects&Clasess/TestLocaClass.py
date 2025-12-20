from Loan import Loan

def main():
    annualInterstRate = eval(input("Enter yearly interest rate, for example 7.25: "))

    numberOfYears = eval(input("Enter number of years  as an integer: "))

    loanAmount = eval(input("Enter loan amount, for example, 12000.95: "))

    borrower = input("Enter borrower's name: ")

    loan  = Loan(annualInterstRate, numberOfYears, loanAmount, borrower)

    print(f"The monthly Payment: {loan.getMothlyPayment():.2f}$")


main()