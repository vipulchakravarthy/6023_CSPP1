# Exercise: PowerIter
# Write a Python function, iterPower(base, exp), that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    product = 1
    for iterate in range (exp):
           product = product * base
    return product   
def main():
    data = input()
    data = data.split()
    print(iterPower(float(data[0]),int(data[1]))) 
if __name__== "__main__":
    main()