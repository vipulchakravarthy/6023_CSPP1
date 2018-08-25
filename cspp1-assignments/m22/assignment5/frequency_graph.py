'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
def frequency_graph(dictionary):
    '''function which prints the keys and values in sorted order and value
    shoud be in form of #
    '''
    for key in sorted(dictionary):
        value = dictionary[key]
        character = "#" * value
        print(key, "-", character)
def main():
    '''the program is to print the keys and values of a dicitonary
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)
if __name__ == '__main__':
    main()
