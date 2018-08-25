'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def main():
    lines = int(input())
    for line in range(lines):
    	text = input()
    	print(text)
if __name__ == '__main__':
    main()
