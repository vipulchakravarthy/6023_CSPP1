'''Exercise : how many
write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.
'''
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    number_values = 0
    for i in aDict.values():
    	number_values += len(i)
    return number_values
def main():
	''' the program is to print the total number of 
	vaules in the total dictionary
	'''
	n=input()
	aDict={}
	for i in range(int(n)):
		s=input()
		l=s.split()
		if l[0][0] not in aDict:
			aDict[l[0][0]]=[l[1]]
		else:
			aDict[l[0][0]].append(l[1])
	print(how_many(aDict))
if __name__== "__main__":
    main()