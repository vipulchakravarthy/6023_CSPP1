'''Exercise : Function and Objects Exercise-3
Implement a function that converts the given testList = [1, -4, 8, -9]
into [1, 16, 64, 81]
'''
def apply_to_each(L, f):
    ''' the function is to print the square of every number in the 
    list.
    '''
    for i in range(len(L)):
         L[i] = square(L[i])
    return L
def square(L):
    return L*L    
def main():
    ''' the program is to print the square of the given 
    numbers in a list
    '''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))
if __name__ == "__main__":
    main()