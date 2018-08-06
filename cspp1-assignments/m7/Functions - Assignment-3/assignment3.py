'''
Functions - Assignment-3 program is to print the what is the lowest
payment done using bisection method
'''
def paying_debtoffinayear(balance_p, annual_interestr):
    ''' the input is taken as balance and annual interest. we calculate the output which
    is the lowest payment value
    '''
    monthly_interestr = (annual_interestr) / 12.0
    monthly_lower = balance_p / 12
    monthly_upper = (balance_p*((1 + monthly_interestr)**12) / 12.0)
    monthly_fixed = (monthly_lower + monthly_upper) / 2.0
    month = 0
    setbal = balance_p
    while  month <= 12:
        month += 1
        monthly_unpaid = balance_p - monthly_fixed
        balance_p = monthly_unpaid + (monthly_interestr * monthly_unpaid)
        if month == 12:
            temp1 = balance_p + 0.03
            temp2 = balance_p - 0.03
            if temp2 <= 0 <= temp1:
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
    ''' the program is to find the lowest payment value using bisection
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", round(paying_debtoffinayear(data[0], data[1]), 2))
if __name__ == "__main__":
    main()
