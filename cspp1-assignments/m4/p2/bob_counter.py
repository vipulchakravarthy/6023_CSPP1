'''Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''
def main():
 """ # the input string is in s
 # remove pass and start your code here """
m_s = str(input())
length_int = len(m_s)
count = 0
for ind in range(length_int-2):
        if m_s[ind] == "b" and m_s[ind+1] == "o" and m_s[ind+2] == "b":
            count += 1
print( count)
if __name__== "__main__":
    main()
