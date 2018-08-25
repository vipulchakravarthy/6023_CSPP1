'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(word_list):
    ''' takes the list of words and gives the dictionary which contains frequency of words
    '''
    for word in word_list:
        word.strip()
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
    character = ':;?,.!@#$'
    lines = int(input())
    word_list = []
    for _ in range(lines):
        row = input().split()
        word_list += row
    for word in word_list:
        for char in character:
            if char in word:
                word = word.replace(char, '')
                word_list.append(word)
    print(tokenize(word_list))
if __name__ == '__main__':
    main()
