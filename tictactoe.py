#Ross Platt
#Tic Tac Toe

def main():

    game = ''
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    while game != 'over':
        
        
        print()
        print_board(board)
        print()
        player_1_choice = int(input('Player 1 choose a space: '))
        winner = 0

        if player_1_choice in board:
            #replace list item with x
            index = player_1_choice - 1
            board[index] = 'X'
        else:
            print('Not an option, loose a turn.')

        if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
            winner = 1
            game = 'over'
        if board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
            winner = 1
            game = 'over'
        if board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
            winner = 1
            game = 'over'
        if board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
            winner = 1
            game = 'over'
        if board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
            winner = 1
            game = 'over'
        if board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
            winner = 1
            game = 'over'
        if board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
            winner = 1
            game = 'over'
        if board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
            winner = 1
            game = 'over'

        if 1 in board or 2 in board or 3 in board or 4 in board or 5 in board or 6 in board or 7 in board or 8 in board or 9 in board:
            if winner == 0:
                print()
                print_board(board)
                print()
                player_2_choice = int(input('Player 2 choose a space: '))
                if player_2_choice in board:
                    #replace list item with x
                    index = player_2_choice - 1
                    board[index] = 'O'
                else:    
                    print('Not an option, loose a turn.')
                
                if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
                    winner = 2
                    game = 'over'
                if board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
                    winner = 2
                    game = 'over'
                if board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
                    winner = 2
                    game = 'over'
                if board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
                    winner = 2
                    game = 'over'
                if board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
                    winner = 2
                    game = 'over'
                if board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
                    winner = 2
                    game = 'over'
                if board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
                    winner = 2
                    game = 'over'
                if board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
                    winner = 2
                    game = 'over'
        else:
            winner = 3
            game = 'over'
            
    if winner != 3:
        print()
        print_board(board)
        print(f'Player {winner} wins!')
    else:
        print()
        print_board(board)
        print('Cat\'s game!')
        

def print_board(list):
    print(f'{list[0]}|{list[1]}|{list[2]}')
    print('-+-+-')
    print(f'{list[3]}|{list[4]}|{list[5]}')
    print('-+-+-')
    print(f'{list[6]}|{list[7]}|{list[8]}')


if __name__ == "__main__":
    main()