'''Exercise : Odd Tuples
Write a python function oddTuples(aTup) that takes a some
numbers in the tuple as input and returns a tuple in which contains
odd index values in the input tuple  
'''
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # return aTup(::2)
    temp = ()
    for i in range(len(aTup)):
        if i %2  == 0 :
             temp += (aTup[i],)
    return temp
def main():
    ''' the given program is to print the elements in odd places 
    of the given list
    '''
    data = input()
    data = data.split()
    aTup=()
    for j in range(len(data)):
        aTup += ((data[j]),)
    print(oddTuples(aTup))
if __name__ == "__main__":
    main()