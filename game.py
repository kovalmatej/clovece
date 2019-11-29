import random

#MAIN GAME FUNCTIONS

def create_game(board_size):
    return generate_board(board_size)[0]

def throw_dice():
    return random.randint(1, 6)

def game_status(counter):
    throwed_number = throw_dice()

    if counter % 2 == 0:
        print("Na rade je hrac A a hodil cislo!", throwed_number)
    else:
        print("Na rade je hrac B!", throwed_number)
    return throwed_number


def start_game(game_board):
    add_figure('A', game_board)
    add_figure('B', game_board)

    counter = 0
    winner = ''

    while(winner == ''):
        number = game_status(counter)
        counter += 1




        draw_board(game_board)

#GAME BOARD FUNCTIONS


def generate_board(n):
    game_board = [[' '] * n for i in range(n)]  # Vytvorí prázdne miesto pre všetky prvky matice
    positions =

    for i in range(n):
        for j in range(n):
            # 1. časť = Selektuje všetky prvky vo vnútornom "krížiku", kde ramená sú dĺžky 3 | 2. časť = Vyhodí vnútro, kde budú domčeky
            if (((n - 3) / 2 <= j <= (n + 1) / 2) & ((j != (n - 1) / 2) & (i != (n - 1) / 2))) | (
                    (i == (n - 1) / 2) & ((j == 0) | (j == n - 1))) | (
                    # Aby horná podmienka nevyhodila konce stredov ramien, tak sa určia vínimky v strede obidvoch cyklov ak je jeden z nich na konci alebo na začiatku
                    (j == (n - 1) / 2) & ((i == 0) | (i == n - 1))):
                game_board[i][j] = '*'
                game_board[j][i] = '*'

            if (j == (n - 1) / 2) & (i != n - 1):  # Vykresli domčeky v strede šachovnice
                game_board[i][j] = 'D'
                game_board[j][i] = 'D'

    game_board[int((n - 1) / 2)][int((n - 1) / 2)] = 'X'
    return [game_board, positions]


def draw_board(game_board):
    for row in game_board:
        print(' '.join([element for element in row]))  # Vypíše všetky elementy v riadku a spojí ich medzerou

def get_positions(game_board):
    32

#PLAYERS FUNCTIONS

def add_figure(player, board):
    if player == 'A':
        if board[0][int((board_size + 1) / 2)] == 'A':
            print('Na štarte už je panáčik hráča A')
        else:
            board[0][int((board_size + 1) / 2)] = 'A'

    if player == 'B':
        if board[int(board_size - 1)][int((board_size - 3) / 2)] == 'B':
            print('Na štarte už je panáčik hráča B')
        else:
            board[int(board_size - 1)][int((board_size - 3) / 2)] = 'B'


board_size = int(input("Zadaj velkost šachovnice"))
current_game = create_game(board_size)

start_game(current_game)
