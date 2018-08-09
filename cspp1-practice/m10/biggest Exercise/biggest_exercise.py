#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    big_key = []
    d = 0
    for i in aDict.keys():
        L = len(aDict[i])
        if L >= d:
            d = L
            big_key += [i]
    return big_key 
def main():
    n = input()
    aDict={}
    for i in range(int(n)):
        s = input()
        l = s.split()
        if l[0][0] not in aDict:
            aDict[l[0][0]]=[l[1]]
        else:
            aDict[l[0][0]].append(l[1])
    print(biggest(aDict))


if __name__== "__main__":
    main()