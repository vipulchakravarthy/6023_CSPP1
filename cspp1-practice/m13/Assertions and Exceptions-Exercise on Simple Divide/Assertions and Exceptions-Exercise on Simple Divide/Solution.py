#define the simple_divide function here
def simple_divide(item, denom):
    try:
        quotient = item/denom
        return quotient
    except:
        raise Exception("0")
        numbers = [0, 0, 0]   
        return numbers
def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]
def main():
    data = input()
    l=data.split()
    l1=[]
    for j in l:
        l1.append(float(j))
    s = input()
    index = int(s)
    print(fancy_divide(l1,index))
if __name__== "__main__":
    main()
