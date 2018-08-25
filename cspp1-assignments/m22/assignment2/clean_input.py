'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    ''' the clean function is to remove the punctuation marks in string
    '''
    character = " !@#$%^'&*()_+/::,.?~"
    for letter in string:
        if letter in character:
            string = string.replace(letter, '')
    return string
def main():
    ''' the program is to clean up the string
    '''
    string = input()
    print(clean_string(string))
if __name__ == '__main__':
    main()
