'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''
def print_dictionary(dictionary):
    '''function which prints the keys and values in sorted order
    '''
    for key in sorted(dictionary):
        print(key, "-" ,dictionary[key])

def main():
    ''' the program is to print the dictionary in a sorted order
    along with the keys and values
    '''
    dictionary = eval(input())
    print_dictionary(dictionary)
if __name__ == '__main__':
    main()
