from playerToPlayer import *
from computer import *

print('')
print('  >>> Welcome to Tic Tac Toe<<<')
print('')

while True:

	board_list = [' '] * 10
	choose = ''
	mode = ''
	turn = ''

	while mode != '1' and mode != '2':
		print('Type 1 for player vs player and 2 for player vs computer')
		mode = input('Enter: ')
	if mode == '1':
		player1_mark, player2_mark = player_input()
		print('\nplayer1 is '+ player1_mark + '\nPlayer2 is '+ player2_mark)
		print('')

		while choose != 'yes' and choose != 'no':
			choose = input('Are you ready to play?\n  Enter "Yes" or "No" : ').lower()
			if choose == 'yes':
				display_board(board_list)
				game_on = True

			else:
				print('')
				game_on = False

		while game_on:

			print('Player 1 turn ')

			player1 = player_choice(board_list)
			place_marker(board_list, player1, player1_mark)
			display_board(board_list)

			if win_check(board_list, player1_mark):
				print('  >>> Conguratulation <<<')
				print('  Player 1 is the winner!!')
				break
				
			elif full_board_check(board_list):
				print('')
				print('  >>> The game is draw! <<<')
				break
			else:
				pass

			print('Player 2 turn ')

			player2 = player_choice(board_list)
			place_marker(board_list, player2, player2_mark)
			display_board(board_list)
			if win_check(board_list, player2_mark):
				print('  >>> Conguratulation <<<')
				print('  Player 2 is the winner!!')
				game_on = False
					
			elif full_board_check(board_list):
				display_board(board_list)
				print('')
				print('  >>> The game is draw! <<<')
				break
			else:
				pass
	else:
		player_mark, pc_mark = player_input()
		print('\nYor are '+ player_mark + '\nComputer is '+ pc_mark)

		while choose != 'player' and choose != 'computer' :
			print('')
			print('Who want to go first? \nType "Player" for player\nType "Computer" for computer')
			choose = input('Enter: ').lower()
			print('')
			if choose == 'player':
				turn = 'player'
			else:
				turn = 'computer'

		while True:
			if turn == 'player':
				print('  Your turn')

				player = player_choice(board_list)
				place_marker(board_list, player, player_mark)
				display_board(board_list)

				if win_check(board_list, player_mark):
					print('  >>> Conguratulation <<<')
					print('  You are the winner!!')
					break
					
				elif full_board_check(board_list):
					print('')
					print('  >>> The game is draw! <<<')
					break
				else:
					turn = 'computer'
			else:
				print('  Computer turn')
				computer = pc_move(board_list, pc_mark, player_mark)
				place_marker(board_list, computer, pc_mark)
				display_board(board_list)

				if win_check(board_list, pc_mark):
					print('  >>> You loose <<<')
					print('  Better luck next time!')
					break

				elif full_board_check(board_list):
					print('')
					print('  >>> The game is draw!')
					break
				
				else:
					turn = 'player'




	if not replay():
		print('  >>> Have a nice day <<<')
		break

