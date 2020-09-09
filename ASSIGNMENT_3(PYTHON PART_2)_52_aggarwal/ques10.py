def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])
def player_input():
    marker = ''
    while marker != 'x' and marker !='o':
        marker = input('playa 1, choose x or o: ')
    playa1 = marker
    if playa1 == 'x':
        playa2 = 'o'
    else:
        playa2 = 'x'
    return (playa1, playa2)
def place_marker(board, marker, position):
    board[position] = marker
def win_check(board, mark):
    return ((board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))
import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
def space_check(board, position):
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True #board is full#
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position 1-9 '))
    
    return position
def replay():
    return input('Play again? enter Y or N ').startswith('y')
print('Welcome to Tic Tac Toe Game!')
print('Be Ready To Enjoy It!')
while True:   
    # Set the game up here (board, who first, choose markers X,O)
    the_board = [' '] * 10
    playa1_marker, playa2_marker = player_input()
    
    turn = choose_first()
    print(turn + 'will go first')
    
    play_game = input('Ready to play? y or n')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
   # Play the game 
    while game_on:
        if turn == 'Player 1': #Player 1 Turn
            
            display_board(the_board)#show the board
            position = player_choice(the_board)#choose position
            place_marker(the_board, playa1_marker, position)
            
            #check if they won 
            if win_check(the_board, playa1_marker):
                display_board(the_board)
                print('Player 1 has won!!')
                game_on = False
            #check if its a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game')
                    break
                else:
                    turn = 'Player 2' #no tie and no win  next player turn
        else:
             #show the board  # Player2's turn.
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, playa2_marker, position)
            
            #check if they won 
            if win_check(the_board, playa2_marker):
                display_board(the_board)
                print('Player 2 has won!!')
                game_on = False
            #check if its a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game')
                    break
                else:
                    turn = 'Player 1' #no tie and no win  next player turn          
#if not replay():
    if not replay():
        break