'''
#Assume s is a string of lower case characters.Write a program that
#prints the number of times the string 'bob' occurs in s.
'''
def main():
  '''
  #the program is to check how many times
  #bob is printed in given string
  '''
  m_sent = str(input())
  length_m = len(m_sent)
  count_var = 0
  for ind in range(length_m-2):
    if m_sent[ind] == "b" and m_sent[ind+1] == "o" and m_sent[ind+2] == "b":
        count_var += 1
print(count_var)
if __name__ == "__main__":
    main()
