'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def main():
    ''' program is to print given text as a  string
    '''
    lines = int(input())
    for _ in range(lines):
        text = input()
        print(text)
if __name__ == '__main__':
    main()
