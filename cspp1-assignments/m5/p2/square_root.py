# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
def main():
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

if __name__== "__main__":
    main()
