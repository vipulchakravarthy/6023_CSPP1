# Functions - Assignment-3 - Using Bisection Search to Make the Program Faster

# You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running
# your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01).
# Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances
# and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission
# is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining
# about too much time taken.)

# Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow
# code?
# We can make this program run faster using a technique introduced in lecture - bisection search!

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What
# is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that. If there was no interest,
# the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month.
# One-twelfth of the original balance is a good lower bound.

# What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we
# ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance
# we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its
# interest compounded monthly for an entire year.

def paying_debtoffinayear(balance_p, annual_interestr):
    monthly_interestr = (annual_interestr) / 12.0
    monthly_lower = balance_p/ 12
    monthly_upper = (balance_p*((1 + monthly_interestr)**12)/ 12.0)
    monthly_fixed = (monthly_lower + monthly_upper) / 2.0
    month = 0
    setbal=balance_p
    while  month<=12:
        month+=1
        monthly_unpaid = balance_p - monthly_fixed
        balance_p = monthly_unpaid + (monthly_interestr* monthly_unpaid)
        if month==12:
            temp1 = balance_p + 0.03
            temp2 = balance_p - 0.03
            if temp2 <=0 <= temp1:
                return monthly_fixed
            elif balance_p < 0:
                balance_p = setbal
                month = 0
                monthly_upper = monthly_fixed
                monthly_fixed = (monthly_lower + monthly_upper) / 2.0
            elif balance_p > 0:
                balance_p = setbal
                month = 0
                monthly_lower = monthly_fixed
                monthly_fixed = (monthly_lower + monthly_upper) / 2.0

def main():
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(round(paying_debtoffinayear(data[0],data[1]),2))
if __name__ == "__main__" :
    main()
