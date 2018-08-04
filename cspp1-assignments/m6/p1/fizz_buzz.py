'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of
the number.
'''
def main():
    '''
    program is to print 1 to n number and if number is divisible by 3 print Fizz
    and if it is divisible by 5 print Buzz and if it is done by both print Fizz Buzz.
    '''
    number = int(input())
    for num_n in range(1, number+1):
        if num_n%3== 0 and num_n%5 == 0:
            print("Fizz")
            print("Buzz")
        elif num_n%3 == 0:
            print("Fizz")
        elif num_n%5 == 0:
            print("Buzz")
        else:
            print(num_n)
if __name__  == "__main__":
    main()

