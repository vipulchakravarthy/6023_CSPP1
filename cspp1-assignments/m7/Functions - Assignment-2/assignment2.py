'''
Assignment-2 - Paying Debt off in a Year
Now write a program that calculates the minimum fixed monthly payment
needed in order pay off a credit card balance within 12 months.
By a fixed monthly payment, we mean a single number which does not change
each month, but instead is a constant amount that will be paid each month.
In this problem, we will not be dealing with a minimum monthly payment rate.
The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
The program should print out one line: the lowest monthly payment that will pay
off all debt in under 1 year
'''
def paying_debtoffinayear(balance_p, annual_interestrate, set_min):
    ''' calculating the minimum lowest payment to be done
    '''
    if balance_p <= 0:
        minimum_fixed = 0
        return minimum_fixed
    minimum_fixed = 10
    month = 0
    monthly_interest = (annual_interestrate) / 12.0
    while  month <= 12:
        month += 1
        monthly_unpaid = balance_p - minimum_fixed
        balance_p = monthly_unpaid + (monthly_interest * monthly_unpaid)
        if monthly_unpaid <= 0 and month == 12:
            return minimum_fixed
        if month == 12 and  monthly_unpaid > 0:
            month = 0
            minimum_fixed += 10
            balance_p = set_min
def main():
    ''' assumin the minimum fixed amount as some number and checking when
    the monthly unpaid is going to be negative so that it will be the lowest
    payment
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", paying_debtoffinayear(data[0], data[1], data[0]))
if __name__ == "__main__":
    main()
