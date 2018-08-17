'''
    Document Distance - A detailed description is given in the PDF
'''
import math
FILENAME = "stopwords.txt"

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    temp1 = {}
    temp2 = {}
    sum1 = 0
    sum_d1 = 0
    sum_d2 = 0
    for word in dict1:
        if word in temp1:
            temp1[word] += 1
        else:
            temp1[word] = 1
    for word in dict2:
        if word in temp2:
            temp2[word] += 1
        else:
            temp2[word] = 1
    word_freq = {}
    keys = set(list(temp1.keys()) + list(temp2.keys()))
    for key in keys:
        word_freq[key] = [0, 0]
    for key in temp1:
        word_freq[key][0] = temp1[key]
    for key in temp2:
        word_freq[key][1] = temp2[key]
    for key in word_freq:
        sum1 = sum1 + (word_freq[key][0] * word_freq[key][1])
    numerator = sum1
    for key in word_freq:
        sum_d1 = sum_d1 + (word_freq[key][0]**2)
        sum_d2 = sum_d2 + (word_freq[key][1]**2)
    denominator = (math.sqrt(sum_d1) * math.sqrt(sum_d2))
    document_distance = numerator/ denominator
    return round(document_distance, 1)
def load_stopwords(file_name):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(file_name, 'r') as file_name:
        for line in file_name:
            stopwords[line.strip()] = 0
    return stopwords
def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = str.lower(input())
    input2 = str.lower(input())
    character = '.,!?$%^&*()1234567890'
    for char in character:
        input1 = input1.replace(char, '')
        input2 = input2.replace(char, '')
    input_list1 = input1.split()
    input_list2 = input2.split()
    stop_words = load_stopwords(FILENAME)
    for word in input_list1:
        if word in stop_words.keys():
            input_list1.remove(word)
    for word in input_list2:
        if word in stop_words.keys():
            input_list2.remove(word)
    print(similarity(input_list1, input_list2))
if __name__ == '__main__':
    main()
