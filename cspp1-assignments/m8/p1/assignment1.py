'''
Exercise: Assignment-1
Write a Python function, factorial(n), that takes in one number
and returns the factorial of given number.
This function takes in one number and returns one number.
'''
def factorial(n):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
def main():
    ''' program is to find the factorial of given number
    using recursion
    '''
    n = int(input())
    print(factorial(n))
if __name__ == "__main__":
    main()
