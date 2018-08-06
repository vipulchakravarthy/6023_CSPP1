'''Functions | Assignment-1 - Paying Debt off in a Year
Write a program to calculate the credit card balance after one year if a person only
pays the minimum monthly payment required by the
credit card company each month. The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal
For each month, calculate statements on the monthly payment and remaining balance.
At the end of 12 months, print out the remaining
balance. Be sure to print out no more than two decimal digits of accuracy - so print
'''
def payingDebtOffInAYear(balance, annualInterestRate, monthlyPaymentRate):
    ''' taking input as balance, annualinterest rate, monthly payment rate and
      and give the remaining balance after one year.
     '''
    month = 0
    while month<= 11:
       monthly_interestR = (annualInterestRate/12.0)
       min_monthlyp = (monthlyPaymentRate*balance)
       monthly_unpaid = balance - min_monthlyp
       balance = monthly_unpaid + (monthly_interestR * monthly_unpaid)
       month+=1
    return round(balance, 2)
def main():
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance: ",(payingDebtOffInAYear(data[0],data[1],data[2])))
if __name__== "__main__":
    main()

