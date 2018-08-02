'''
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
#your program should print:
#Number of vowels: 5
'''
def main():
    '''
    #Write a program that counts up the number of vowels contained in the string s.
    #Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
    '''
    s_in = str(input())
    s_input = s_in.lower()
    count_int = 0
    for char in s_input:
        if char  in ('a', 'e', 'i', 'o', 'u'):
            count_int += 1
    print(count_int)
    # the input string is in s
    # remove pass and start your code here
    pass

if __name__ == "__main__":
    main()
    