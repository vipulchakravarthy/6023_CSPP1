'''
#Assume s is a string of lower case characters.Write a program
#that prints the longest substring of s in which the letters occur in
#alphabetical order.In the case of ties, print the first substring.
'''
def main():
    ''' 
         #the program is to print longest substring in the given string
    '''
    imp_sentence = str(input())
    imp_sent = str.lower(imp_sentence)
    maxim_substr = []
    for i in range(len(imp_sent)):
        sub_string = imp_sent[i]
        count_var = 0
        while i + 1 < len(imp_sent) and imp_sent[i] <= imp_sent[i+1]:
            count_var += 1
            i += 1
            sub_string += imp_sent[i]
        if len(sub_string) > len(maxim_substr):
            maxim_substr = sub_string
    print(maxim_substr)
    # the input string is in s
    # remove pass and start your code here
if __name__ == "__main__":
    main()
