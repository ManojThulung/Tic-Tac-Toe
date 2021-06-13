
import os

def display_board(board):
	os.system('cls')
	print('	 '+board[1]+' | '+board[2]+' | '+board[3])
	print('	---|---|---')
	print('	 '+board[4]+' | '+board[5]+' | '+board[6])
	print('	---|---|---')
	print('	 '+board[7]+' | '+board[8]+' | '+board[9])

#board_list = [' ']*10 #['#','X','O','X','O','X','O','X','O','X']
#display_board(board_list)

def player_input():
	player1 = ''
	print('Choose either "X" pr "O".')
	while player1 != 'X' and player1 != 'O':
		player1 = input("Choose your marker: ").upper()
		if player1 == 'X':
			#rint('\nplayer1 is X\nPlayer2 is O\n')
			return ('X','O')

		elif player1 == 'O':
			#print('\nplayer1 is O\nPlayer2 is X\n')
			return ('O','X')
		else:
			print("\nplase enter the correct given marker.")

#player_input()

def place_marker(board, position, marker):
	board[position] = marker
#place_marker(board_list,'X',1)
#display_board(board_list)

def win_check(board, marker):
	return (board[1] == board[2] == board[3] == marker) or \
	(board[4] == board[5] == board[6] == marker) or \
	(board[7] == board[8] == board[9] == marker) or \
	(board[1] == board[4] == board[7] == marker) or \
	(board[2] == board[5] == board[8] == marker) or \
	(board[3] == board[6] == board[9] == marker) or \
	(board[1] == board[5] == board[9] == marker) or \
	(board[3] == board[5] == board[7] == marker)
#print(win_check(board_list,' '))


def space_check(board, position):
	return board[position] == ' '
#print(space_check(board_list, 9))


def full_board_check(board):
	for i in range(1, 10):
		if space_check(board, i):
			return False
	return True
#print(full_board_check())

def player_choice(board):
	position = 0
	while position not in [1,2,3,4,5,6,7,8,9]:
		try:
			position = int(input("Enter the position 1-9: "))
			if position > 9 or position < 0:
				print('')
				print('Plase enter the number 1-9')
				position = 0

			elif board[position] != ' ':
				print('')
				print('The filed is already used')
				position = 0
		except ValueError:
			print('')
			print('Please enter appropriate value.')
	return position
#print(player_choice(board_list))


def replay():
	replay = ''
	print('')
	print('Do you want to play again?')
	while replay != 'yes' and replay != 'no':
		replay = input("  Type 'Yes' or 'No': ").lower()
	
	return replay == 'yes'

