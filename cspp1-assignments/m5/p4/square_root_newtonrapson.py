''' Write a python program to find the square root of the given
number using newton-raphson method
'''
def main():
    ''' the problem is to find square root of a given number
    using newton-raphson method.
    '''
    number = int(input())
    epsilon = 0.01
    check = (number / 2.0)
    while abs(check**2 - number) >= epsilon:
        check = check - ((check**2 - number) / (2*check))
    print(check)
if __name__ == "__main__":
    main()
