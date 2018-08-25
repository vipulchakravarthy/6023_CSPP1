'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(word_list):
	''' takes the list of words and gives the dictionary which contains frequency of words
	'''
    dictionary = {}
    for iterate in word_list:
    	if iterate in dictionary:
    		dictionary[iterate] += 1
    	else:
    		dictionary[iterate] = 1
    return dictionary       
def main():
	''' to take the input and give the frequency of words in that string
	'''
	lines = int(input())
	for _ in range(lines):
		word_list = input().split()
	print(tokenize(word_list))
if __name__ == '__main__':
    main()
