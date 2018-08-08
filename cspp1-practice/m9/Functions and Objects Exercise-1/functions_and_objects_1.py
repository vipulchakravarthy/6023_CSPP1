'''Exercise : Function and Objects Exercise-1
Implement a function that converts the given testList = [1, -4, 8, -9]
into [1, 4, 8, 9]
'''
def apply_to_each(L, f):
	''' function is to do the required assignment for
	each and every element
	''' 
    for i in range(len(L)):
        L[i] = f(L[i])
    return L
def main():
	''' input is taken as a list of numbers and output is 
	absolute of those numbers
	'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, abs))
if __name__ == "__main__":
    main()
