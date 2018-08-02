'''Assume s is a string of lower case characters. Write a program 
that prints the longest substring of s in which the letters occur in 
alphabetical order.Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring.
'''
def main():
 ''' 
 #the program is to print longest substring 
 #in the given string
 '''
s_sentence = str(input())
s_sent = str.lower(s_sentence)
maxi_substr = []
for i in range(len(s_sent)):
    sub_string = s_sent[i]
    count_var = 0
    while i + 1 < len(s_sent) and s_sent[i] <= s_sent[i+1]:
            count_var+= 1
            i+=1
            sub_string += s_sent[i]
    if len(sub_string) > len(maxi_substr):
        maxi_substr = sub_string
print(maxi_substr)
    # the input string is in s
    # remove pass and start your code here
if __name__== "__main__":
    main()
