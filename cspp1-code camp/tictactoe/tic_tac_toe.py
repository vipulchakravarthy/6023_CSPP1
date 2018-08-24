'''
the program is to play tic tac toe game 
and decide the winner
'''
from collections import Counter
def is_winner(tic_list):
    '''
    takes a list as input and returns who is the winner
    '''
    count = 0
    flag = 0
    count_dict = Counter()
    for iterate in tic_list:
        for char in iterate:
            count_dict[char] += 1
    for row in range(3):
        for column in range(3):
            if (tic_list[row][column] != 'x' and tic_list[row][column] != 'o'
                    and tic_list[row][column] != '.'):
                flag = 1
    if flag == 1:
        return "invalid input"
    if count_dict['x'] > 5 or count_dict['o'] > 5:
        return "invalid game"
    if (tic_list[0][0] == tic_list[0][1] == tic_list[0][2] == 'x' or
            tic_list[1][0] == tic_list[1][1] == tic_list[1][2] == 'x' or
            tic_list[2][0] == tic_list[2][1] == tic_list[2][2] == 'x' or
            tic_list[0][0] == tic_list[1][1] == tic_list[2][2] == 'x' or
            tic_list[0][0] == tic_list[1][0] == tic_list[2][0] == 'x' or
            tic_list[0][2] == tic_list[1][1] == tic_list[2][0] == 'x' or
            tic_list[0][2] == tic_list[1][2] == tic_list[2][2] == 'x' or
            tic_list[0][1] == tic_list[1][1] == tic_list[2][1] == 'x'):
        count += 1
        winner = 'x'
    if (tic_list[0][0] == tic_list[0][1] == tic_list[0][2] == 'o' or
            tic_list[1][0] == tic_list[1][1] == tic_list[1][2] == 'o' or
            tic_list[2][0] == tic_list[2][1] == tic_list[2][2] == 'o' or
            tic_list[0][0] == tic_list[1][1] == tic_list[2][2] == 'o' or
            tic_list[0][0] == tic_list[1][0] == tic_list[2][0] == 'o' or
            tic_list[0][2] == tic_list[1][1] == tic_list[2][0] == 'o' or
            tic_list[0][2] == tic_list[1][2] == tic_list[2][2] == 'o' or
            tic_list[0][1] == tic_list[1][1] == tic_list[2][1] == 'o'):
        count += 1
        winner = 'o'
    if count == 2:
        return "invalid game"
    if count == 0:
        winner = "draw"
    return winner

def main():
    '''
    the program is to decide the winner of tic tac toe game
    '''
    tic_list = []
    for _ in range(3):
        row = list(map(str, input().split()))
        tic_list.append(row)
    print(is_winner(tic_list))
if __name__ == '__main__':
    main()
