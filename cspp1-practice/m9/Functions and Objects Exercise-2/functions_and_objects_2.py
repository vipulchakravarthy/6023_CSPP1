'''Exercise : Function and Objects Exercise-2
Implement a function that converts the
given testList = [1, -4, 8, -9] into [2, -3, 9, -8]
'''
def apply_to_each(L, f):
    ''' increment by one value for all the elements in
    the list
    '''
    for i in range(len(L)):
         L[i] = increment(L[i])
    return L
def increment(L):
    L +=1
    return L
def main():
    ''' if the input is a list then the output will be increment of every 
    value in that given list
    '''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1,increment))
if __name__ == "__main__":
    main()
