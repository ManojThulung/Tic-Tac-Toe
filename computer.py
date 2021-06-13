from playerToPlayer import *

import random

def random_number(board):
	choose = random.choice([1,3,7,9])
	
	while board[choose] != ' ':
		choose = random.choice([1,3,7,9])

	while board[choose] != ' ':
		choose = random.randint(2,9)
	return choose

def copy(board_list):
	dub = []
	for i in board_list:
		dub.append(i)
	return dub

def pc_move(board_list, pc_mark, player):
	cop = copy(board_list)
	for i in range(1, 10):
		cop = copy(board_list)
		if space_check(board_list, i):
			place_marker(cop, i, pc_mark)
			if win_check(cop, pc_mark):
				return i
	
	for i in range(1, 10):
		cop = copy(board_list)
		if space_check(board_list, i):
			place_marker(cop, i, player)
			if win_check(cop, player):
				return i

	return random_number(board_list)

board_list = [' ','x','o','x','x','o',' ','o','x','o']
pc_mark = 'x'
player = 'o'
#print(pc_move(board_list, pc_mark, player))
#print(random_number(board_list))


