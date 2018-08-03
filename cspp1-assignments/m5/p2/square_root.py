''' Write a python program to find the square root of the
given number using approximation method.
'''
def main():
    ''' the problem given is to find the square root of the
    given number using approximation
    '''
    number = int(input())
    epsilon = 0.01
    step = 0.1
    check = 0.0
    while check <= number:
        if abs(check**2 - number) >= epsilon:
            check += step
        else:
            break
    print(check)
if __name__ == "__main__":
    main()