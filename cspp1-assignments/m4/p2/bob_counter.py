'''Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''
def main():
"""the input string is in s remove pass and start your code here"""
main_string = str(input())
length_string = len(m_s)
count_var = 0
for ind in range(length_string-2) :
  if main_string[ind] == "b" and main_string[ind+1] == "o" and main_string[ind+2] == "b":
    count_var += 1
print( count_var)
if __name__ == "__main__":
    main()
