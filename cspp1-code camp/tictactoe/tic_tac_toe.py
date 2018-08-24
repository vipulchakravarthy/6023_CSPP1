from collections import Counter 
def is_winner(tic_list):
	count = 0
	flag = 0
	for i in range(3):
		for j in range(3):
			if tic_list[i][j] != 'x' and tic_list[i][j] != 'o' and tic_list[i][j] != '.':
				flag = 1
	if flag == 1:
		return "invalid input"
	if (tic_list[0][0] == tic_list[0][1] == tic_list[0][2] == 'x' or
		tic_list[1][0] == tic_list[1][1] == tic_list[1][2] == 'x' or
		tic_list[2][0] == tic_list[2][1] == tic_list[2][2] == 'x' or
		tic_list[0][0] == tic_list[1][1] == tic_list[2][2] == 'x' or
		tic_list[0][0] == tic_list[1][0] == tic_list[2][0] == 'x' or
		tic_list[0][2] == tic_list[1][1] == tic_list[2][0] == 'x' or
		tic_list[0][2] == tic_list[1][2] == tic_list[2][2] == 'x' or
		tic_list[0][1] == tic_list[1][1] == tic_list[2][1] == 'x' ):
		count += 1
		winner =  'x'
	if (tic_list[0][0] == tic_list[0][1] == tic_list[0][2] == 'o' or
		tic_list[1][0] == tic_list[1][1] == tic_list[1][2] == 'o' or
		tic_list[2][0] == tic_list[2][1] == tic_list[2][2] == 'o' or
		tic_list[0][0] == tic_list[1][1] == tic_list[2][2] == 'o' or
		tic_list[0][0] == tic_list[1][0] == tic_list[2][0] == 'o' or
		tic_list[0][2] == tic_list[1][1] == tic_list[2][0] == 'o' or
		tic_list[0][2] == tic_list[1][2] == tic_list[2][2] == 'o' or
		tic_list[0][1] == tic_list[1][1] == tic_list[2][1] == 'o' ):
		count += 1
		winner = 'o'
	if count == 2:
		return "invalid game"
	return winner
	# count_dict = Counter()
	# for i in tic_list:
	# 	for x in i:
	# 		count_dict[x] += 1
	# print(count_dict)
def main():
	tic_list = []
	for i in range(3):
		row = list(map(str,input().split()))
		tic_list.append(row)
	print(is_winner(tic_list))
if __name__ == '__main__':
    main()


