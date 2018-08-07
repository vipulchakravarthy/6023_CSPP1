'''
Exercise: Assignment-2
Write a Python function, sumofdigits, that takes in 
one number and returns the sum of digits of given number.
This function takes in one number and returns one number.
'''
def sumofdigits(n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if number_g <= 0:
        return 0
    return (number_g % 10) + sumofdigits(number_g // 10)
def main():
    ''' program is to calculate the sum of the digits of
    a given number and print the sum using functions
    '''
    a = input()
    print(sumofdigits(int(a)))
if __name__ == "__main__":
    main()

