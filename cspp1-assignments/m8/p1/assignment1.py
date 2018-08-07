'''
Exercise: Assignment-1
Write a Python function, factorial(n), that takes in one
number and returns the factorial of given number.
This function takes in one number and returns one number.
'''
def factorial(num_g):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if num_g == 1 or num_g == 0:
        return 1
    if num_g > 1:
        return num_g * factorial(num_g -1)
def main():
    ''' program is to find the factorial of given number
    '''
    number = int(input())
    print(factorial(number))
if __name__ == "__main__":
    main()
