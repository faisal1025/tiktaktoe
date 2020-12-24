# First step is to create board
board = [' ' for x in range(10)]

def insert_letter(letter, pos):              #this function insert letter[x/o] on given position
    board[pos] = letter

def space_is_free(pos):
    return board[pos] == ' '

def print_board(board):
    print('   |     | ')
    print('' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] + ' ')
    print('   |     | ')
    print('---------------')
    print('   |     | ')
    print('' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] + ' ')
    print('   |     | ')
    print('---------------')
    print('   |     | ')
    print('' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] + ' ')
    print('   |     | ')

def is_winner(bo, le):
    return (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le) or (bo[1] == le and bo[5] == le and bo[9] == le)

def player_move():
    turn = True
    while turn:
        move = input('Choose the position between [1-9] where you want to put your next step as [X]')
        try:
            move = int(move)
            if (move > 0 and  move < 10):
                if space_is_free(move):
                    turn = False
                    insert_letter('X', move)
                else:
                    print('Sorry!! That space is already captured... choose available position')
            else:
                print('Give a position in range')
        except:
            print('Oops!!Please insert an integer :-@')

def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ']
    move = 0
    for let in ['O', 'X']:
        for i in possible_moves:
            boardCopy = board[:]
            boardCopy[i] = let
            if is_winner(boardCopy, let):
                move = i
                return move
            
    if 5 in possible_moves:
        move = 5
        return move

    cornersOpens = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            cornersOpens.append(i)
    if len(cornersOpens) > 0:
        move = select_random(cornersOpens)
        return move

    edgesOpens = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            edgesOpens.append(i)
    if len(edgesOpens) > 0:
        move = select_random(edgesOpens)

    return move

def select_random(li):
    import random
    le = len(li)
    r = random.randrange(0, le)
    return li[r]

def is_board_full():
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    while not (is_board_full()):
        if not (is_winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print('You lose :-( . better luck next time')
            break
        if not (is_winner(board, 'X')):
            move = comp_move()
            if move == 0:
                break
            else:
                insert_letter('O', move)
                print('computer make an \'O\' in position ', move, ':')
                print_board(board)
        else:
            print('Good job! \'X\' won the game ;-)')
            break
    if is_board_full():
        print('Tie game!!')

play = True
while play:
    print_board(board)
    main()
    choice = input('do you want to play again[yes/no]')
    if choice == 'no':
        play = False
    if choice == 'yes':
        board = [' ' for x in range(10)]
