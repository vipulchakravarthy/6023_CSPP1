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
    character = ":;?,.''!@#$"
    lines = int(input())
    word_list = []
    for _ in range(lines):
        row = input().split()
        word_list += row
    temp_list = word_list[:]
    for word in word_list:
        print(word)
        for char in character:
            print(char)
            if char in word:
                word = word.replace(char, '')
                print(word)
                word_list = word_list.append(word)
    print(word_list)
    print(tokenize(temp_list))
if __name__ == '__main__':
    main()
