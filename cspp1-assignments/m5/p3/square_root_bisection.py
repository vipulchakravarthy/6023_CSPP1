'''# Write a python program to find the square root of the
given number using bisection method
'''
def main():
   ''' the problem is to find square root of a number using
    bisection method
   '''
    epsilon = 0.01
    number = int(input())
    low = 0.0
    high = number
    output = (low + high)/2.0
    while abs(output**2 - number) >= epsilon:
        if output**2 < number:
            low = output
        else:
            high = output
        output = (low + high)/2.0
    print(output)
if __name__ == "__main__":
    main()
