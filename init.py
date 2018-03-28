
is_player_1_turn = True
pieces = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
finished = False


def select_team():
    print('WELCOME TO THE TIC TAC TOE GAME!!!')
    success = False
    players = {}
    while not success:
        players['p1'] = input('Select team x or o \n')
        if players['p1'] == 'o' or players['p1'] == 'x':
            success = True
    if players['p1'] == 'x':
        players['p2'] = 'o'
    else:
        players['p2'] = 'x'
    return players


def print_board(pieces):
    print(f' {pieces[6]} | {pieces[7]} | {pieces[8]} \n')
    print('_____________\n')
    print(f' {pieces[3]} | {pieces[4]} | {pieces[5]} \n')
    print('_____________\n')
    print(f' {pieces[0]} | {pieces[1]} | {pieces[2]} \n')


def put_piece():
    c = players['p1'] if is_player_1_turn else players['p2']
    valid_selection = False
    player = get_player()
    while not valid_selection:
        num = int(input(f"{player}: Put the piece in an empty space (choose a number between 0 and 9 to set the piece)\n"))
        if num in range(0, 10):
            valid_selection = True
    pieces[num - 1] = c
    print_board(pieces)


def get_player():
    if is_player_1_turn:
        return 'Player 1'
    else:
        return 'Player 2'


def check_fin():
    if is_player_1_turn:
        c = players['p1']
    else:
        c = players['p2']
    if ((pieces[0] == pieces[1] == pieces[2] == c) or
    (pieces[3] == pieces[4] == pieces[5] == c) or
    (pieces[6] == pieces[7] == pieces[8] == c) or
    (pieces[0] == pieces[3] == pieces[6] == c) or
    (pieces[1] == pieces[4] == pieces[7] == c) or
    (pieces[2] == pieces[5] == pieces[8] == c) or
    (pieces[0] == pieces[4] == pieces[8] == c) or
    (pieces[2] == pieces[4] == pieces[6] == c)):
        return True
    else:
        return False


players = select_team()
print(f'Player 1 plays with {players["p1"]} and player 2 plays with {players["p2"]}')
print_board(pieces)
while not finished:
    put_piece()
    finished = check_fin()
    if finished:
        break
    is_player_1_turn = not is_player_1_turn

winner = get_player()
print(f'{winner} has won')

