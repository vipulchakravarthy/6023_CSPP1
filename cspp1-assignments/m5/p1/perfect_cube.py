''' Write a python program to find if the given number is a
perfect cube or not using guess and check algorithm
'''
def main():
    ''' the problem is about to check whether the given
     number is perfect cube or not
     '''
    cube_number = int(input())
    epsilon = 0.01
    step = 1
    guess = 0
    while guess <= cube_number:
        if abs(guess**3 -cube_number) >= epsilon:
            guess += step
        else:
            break
    if abs(guess**3 - cube_number) >= epsilon:
        print(str(cube_number) + ' is not a perfect cube')
    else:
        print(str(cube_number) + ' is a perfect cube ')
if __name__ == "__main__":
    main()
