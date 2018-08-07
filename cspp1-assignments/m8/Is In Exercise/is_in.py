'''
Exercise: Is In Write a Python function, isIn(char, aStr), that 
takes in two arguments a character and String and returns the isIn(char, aStr)
which retuns a boolean value.This function takes in two arguments 
character and String and returns one boolean value.
'''
def isitIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    temp = ''
    if aStr == '': 
        return False
    temp = sorted(aStr)
    m = temp[len(temp) // 2]
    if char == m:
        return True
    elif len(temp) == 0:
        return False
    elif char < m:
        return isitIn(char, temp[:len(temp) // 2])
    else:
        return isitIn(char, temp[len(temp) // 2:])
    return isitIn(char, aStr)
def main():
    ''' the program is to check whether the given character is
    present in given string or not
    '''
    data = input()
    data = data.split()
    print(isitIn((data[0][0]), data[1]))
if __name__== "__main__":
    main()