import random

#MAIN GAME FUNCTIONS

def create_game(board_size):
    return generate_board(board_size)

def throw_dice():
    return random.randint(1, 6)

def game_status(counter):
    throwed_number = throw_dice()

    if counter % 2 == 0:
        print("Na rade je hrac A a hodil cislo: ", throwed_number)
    else:
        print("Na rade je hrac B a hodil cislo: ", throwed_number)
    return throwed_number


def start_game(game_board):
    add_figure('A', game_board)
    add_figure('B', game_board)

    figures1 = [[0, int((board_size - 1) / 2 + 1)]]
    figures2 = [[board_size - 1, int((board_size - 1) / 2 - 1)]]

    counter = 0
    winner = ''

    while(winner == ''):
        number = game_status(counter)
        if counter % 2 == 0:
            if len(figures1) == 1:
                moveFigure(game_board,'A', figures1[0], number, figures1)
        if counter % 2 == 1:
            if len(figures2) == 1:
                moveFigure(game_board,'B', figures2[0], number, figures2)

        counter += 1


        draw_board(game_board)

#GAME BOARD FUNCTIONS


def generate_board(n):
    game_board = [[' '] * n for i in range(n)]  # Vytvorí prázdne miesto pre všetky prvky matice

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

               # positions.append([i, j])

    game_board[int((n - 1) / 2)][int((n - 1) / 2)] = 'X'
    return game_board


def draw_board(game_board):
    for row in game_board:
        print(' '.join([element for element in row]))  # Vypíše všetky elementy v riadku a spojí ich medzerou

def get_positions(game_board):
    positions = []

    for i in range(int((board_size - 1) / 2)):
        for j in range(int((board_size - 1) / 2) + 1, board_size):
            if (game_board[i][j] != ' ') & (game_board[i][j] != 'D') & (game_board[i][j] != 'X'):
                positions.append([i, j])

    positions.append([int((board_size - 1) / 2), board_size - 1])

    for i in range(int((board_size - 1) / 2) + 1, board_size - 1):
        for j in range(board_size - 1, int((board_size - 1) / 2), -1):

            if ((game_board[i][j] != ' ') & (game_board[i][j] != 'D') & (game_board[i][j] != 'X')):
                positions.append([i, j])

    positions.append([board_size - 1, int((board_size - 1) / 2) + 1])

    for i in range(board_size - 1,int((board_size - 1) / 2), -1):
        for j in range(int((board_size - 1) / 2), 0, -1):
            if ((game_board[i][j] != ' ') & (game_board[i][j] != 'D') & (game_board[i][j] != 'X')):
                positions.append([i, j])

    positions.append([int((board_size - 1) / 2) + 1, 0])

    for i in range(int((board_size - 1) / 2), -1, -1):
        for j in range(0, int((board_size - 1) / 2 )):
            if ((game_board[i][j] != ' ') & (game_board[i][j] != 'D') & (game_board[i][j] != 'X')):
                positions.append([i, j])

    positions.append([0, int((board_size - 1) / 2)])

    return positions


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


def moveFigure (board, player, figure, length, figures):
    positions = get_positions(current_game)

    currentPos = positions.index(figure)
    newPos = currentPos + length

    oldY = positions[currentPos][0]
    oldX = positions[currentPos][1]

    if newPos == 32:
        newPos = 0

    if 32 > newPos:
        y = positions[newPos][0]
        x = positions[newPos][1]
        board[y][x] = str(player)
        board[oldY][oldX] = '*'

    if (32 < newPos < 32 + (board_size - 3) / 2) & (player == 'A') :
        board[newPos - 31][int((board_size - 1) / 2)] = 'A'
        board[oldY][oldX] = '*'

    if(32 < newPos < 32 + (board_size - 3) / 2) & (player == 'B'):
        newPos = newPos - currentPos - (32 - currentPos)
        y = positions[newPos][0]
        x = positions[newPos][1]
        board[y][x] = str(player)
        board[oldY][oldX] = '*'

    if (15 < newPos < 15 + (board_size - 3) / 2) & (player == 'B'):
        print (newPos)
        board[board_size - newPos + 13][int((board_size - 1) / 2)] = 'B'
        board[oldY][oldX] = '*'

    if (len(figures)) & (newPos <= 32) == 1:
        y = positions[newPos][0]
        x = positions[newPos][1]
        figures[0] = [y,x]


#GAME

board_size = int(input("Zadaj velkost šachovnice"))
current_game = create_game(board_size)

start_game(current_game)

print(get_positions(current_game))
