'''
#Assume s is a string of lower case characters.Write a program that
#prints the number of times the string 'bob' occurs in s.
'''
def main():
  '''
  #the program is to check how many times
  #bob is printed in 
  #given 
  #string
  '''
main_string = str(input())
length_string = len(main_string)
count_var = 0
for ind in range(length_string-2):
    if main_string[ind] == "b" and main_string[ind+1] == "o" and main_string[ind+2] == "b":
        count_var += 1
print(count_var)
if __name__ == "__main__":
    main()
