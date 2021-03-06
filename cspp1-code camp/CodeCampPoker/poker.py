'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def values(hand):
    ''' the values function is to make all the face values in one list
    '''
    temp_list = []
    for element in hand:
        if element[0] == 'A':
            temp_list.append(14)
        elif element[0] == 'K':
            temp_list.append(13)
        elif element[0] == 'Q':
            temp_list.append(12)
        elif element[0] == 'J':
            temp_list.append(11)
        elif element[0] == 'T':
            temp_list.append(10)
        else:
            temp_list.append(int(element[0]))
    value = sorted(temp_list)
    return value
def highcard(hand):
    ''' to check whether the given hand is high card or not
    '''
    temp_list = []
    for element in hand:
        if element[0] == 'A':
            temp_list.append(float(1.4))
        elif element[0] == 'K':
            temp_list.append(float(1.3))
        elif element[0] == 'Q':
            temp_list.append(float(1.2))
        elif element[0] == 'J':
            temp_list.append(float(1.1))
        elif element[0] == 'T':
            temp_list.append(float(1.0))
        else:
            temp_list.append(float(element[0])/10)
    return max(temp_list)         

def is_fullhouse(hand):
    ''' calculate whether the given hand is full house or not
    '''
    iterate = 0
    pair_1 = 0
    pair_2 = 0
    while iterate <= (len(hand)-1):
        temp = hand[iterate][0]
        count = 0
        for element in hand:
            if element[0] == temp:
                count += 1
        if count == 3:
            pair_1 = 1
        elif count == 2:
            pair_2 = 1
        iterate += 1
    flag = bool(pair_1 == 1 and pair_2 == 1)
    return flag
def is_twopair(hand):
    ''' calculate whether the given hand is two pair or not
    '''
    iterate = 0
    while iterate <= (len(hand)-1):
        temp = hand[iterate][0]
        count = 0
        for element in hand:
            if element[0] == temp:
                count += 1
        iterate += 1
    flag = bool(count == (len(hand)-1))
    return flag
def is_onepair(hand):
    ''' check whether the given hand is one pair or not
    '''
    # iterate = 0
    # while iterate <= (len(hand)-1):
    #     temp = hand[iterate][0]
    #     count = 0
    #     for element in hand:
    #         if element[0] == temp:
    #             count += 1
    #     if count == (len(hand)-3):
    #         return True
    #     iterate += 1
    # return False
    new = []
    value_list = sorted(values(hand))
    for i in value_list:
        if value_list.count(i) == 2:
            new.append(i)
    if len(new) == 0:
        return False
    return (max(new)/100)+1
def is_three_a_kind(hand):
    ''' check whether the given hand is three a kind or not
    '''
    iterate = 0
    while iterate <= (len(hand)-1):
        temp = hand[iterate][0]
        count = 0
        for element in hand:
            if element[0] == temp:
                count += 1
        if count == (len(hand)-2):
            return True
        iterate += 1
    return False
def is_fourakind(hand):
    ''' check whether given hand is four a kind or not
    '''
    count = 0
    temp = hand[0][0]
    for element in hand:
        if element[0] == temp:
            count += 1
    flag = bool(count == (len(hand)-1))
    return flag
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    count = 0
    temp_list = []
    for element in hand:
        if element[0] == 'A':
            temp_list.append(14)
        elif element[0] == 'K':
            temp_list.append(13)
        elif element[0] == 'Q':
            temp_list.append(12)
        elif element[0] == 'J':
            temp_list.append(11)
        elif element[0] == 'T':
            temp_list.append(10)
        else:
            temp_list.append(int(element[0]))
    value = sorted(temp_list)
    for element in range(len(value)-1):
        if value[element+1]-value[element] == 1:
            count += 1
    flag = bool(count == len(value)-1)
    return flag
def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    count = 0
    temp = hand[0][1]
    for element in hand:
        if element[1] == temp:
            count += 1
    flag = bool(count == len(hand))
    return flag

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    if is_flush(hand) and is_straight(hand):
        return 9
    if is_fourakind(hand):
        return 8
    if is_fullhouse(hand):
        return 7
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    if is_three_a_kind(hand):
        return 4
    if is_twopair(hand):
        return 3
    if is_onepair(hand):
        return is_onepair(hand)
    return highcard(hand)
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)
if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
