'''
Given a  number int_input, find the product of all the digits
example:input: 123 ;output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input
    and print the product its digits.
    '''
    int_input = int(input())
    product = 1
    if int_input == 0:
        product = 0
    while int_input != 0:
        digit = abs(int_input )% 10
        product = product * digit
        int_input = abs(int_input) // 10
    print(product)
if __name__ == "__main__":
    main()
