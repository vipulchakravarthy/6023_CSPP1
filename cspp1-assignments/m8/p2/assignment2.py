'''
Exercise: Assignment-2
Write a Python function, sumofdigits, that takes in one
number and returns the sum of digits of given number.
This function takes in one number and returns one number.
'''
def sumofdigits(number_g):
    '''
    n is positive Integer returns: a positive integer
    the sum of digits of n.
    '''
    sum_n = 0
    while number_g > 0:
        digit = number_g%10
        sum_n = sum_n + digit
        number_g = number_g // 10
    return sum_n
def main():
    ''' program is to calculate the sum of the digits of 
    a given number and print the sum using functions
    '''
    number_g = int(input())
    print(sumofdigits(number_g)) 
if __name__ == "__main__":
    main()

