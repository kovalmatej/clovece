import random


# MAIN GAME FUNCTIONS

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
    figures1 = []
    figures2 = []
    add_figure('A', game_board, figures1)
    add_figure('B', game_board, figures2)
    print (figures1)
    print(figures2)


    counter = 0
    winner = ''
    figures_in_houseA = 0
    figures_in_houseB = 0

    draw_board(game_board)
    while (winner == ''):
        number = game_status(counter)
        choice = 0

        if counter % 2 == 0:
            if number == 6:
                choice = int(input(
                    "Padla 6, zadaj 1 ak chceš pridať nového panáčika, ľubovoľnú inú hodnotu ak chceš pohnúť panáčikom."))
                if (choice == 1):
                    print("pridaná figurka")
                    add_figure('A', game_board, figures1)

            if len(figures1) == 1:
                moveFigure(game_board, 'A', figures1[0], number, figures1, figures_in_houseA)
            elif (choice != 1) | ((len(figures1) != 1) & (choice !=1)):
                x = int(input("Zadaj X súradnicu panáčika, ktorým chceš pohnúť."))
                y = int(input("Zadaj Y súradnicu panáčika, ktorým chceš pohnúť."))

                print (figures1)
                figure = figures1.index([y, x, 0])
                moveFigure(game_board, 'A', figures1[figure], number, figures1, figures_in_houseA)

        if counter % 2 == 1:
            if number == 6:
                choice = int(input(
                    "Padla 6, zadaj 1 ak chceš pridať nového panáčika, ľubovoľnú inú hodnotu ak chceš pohnúť panáčikom."))
                if (choice == 1):
                    add_figure('B', game_board, figures2)

            if len(figures2) == 1:
                moveFigure(game_board, 'B', figures2[0], number, figures2, figures_in_houseB)
            elif(choice != 1) | ((len(figures1) != 1) & (choice !=1)):
                x = int(input("Zadaj X súradnicu panáčika, ktorým chceš pohnúť."))
                y = int(input("Zadaj Y súradnicu panáčika, ktorým chceš pohnúť."))

                print (figures2)
                figure = figures2.index([y, x, 0])
                moveFigure(game_board, 'B', figures2[figure], number, figures2,
                           figures_in_houseB)

        counter += 1

        if figures_in_houseA == 4:
            winner = 'A'
        elif figures_in_houseB == 4:
            winner = 'B'

        draw_board(game_board)


# GAME BOARD FUNCTIONS


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

    game_board[int((n - 1) / 2)][int((n - 1) / 2)] = 'X'
    return game_board


def draw_board(game_board):
    print("   ", end="")
    for i in range(board_size):
        print(i, end=" ")
    print("")

    a = 0
    for row in game_board:
        print(a, "", end=" ")
        a += 1
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

    for i in range(board_size - 1, int((board_size - 1) / 2), -1):
        for j in range(int((board_size - 1) / 2), 0, -1):
            if ((game_board[i][j] != ' ') & (game_board[i][j] != 'D') & (game_board[i][j] != 'X')):
                positions.append([i, j])

    positions.append([int((board_size - 1) / 2) + 1, 0])

    for i in range(int((board_size - 1) / 2), -1, -1):
        for j in range(0, int((board_size - 1) / 2)):
            if ((game_board[i][j] != ' ') & (game_board[i][j] != 'D') & (game_board[i][j] != 'X')):
                positions.append([i, j])

    positions.append([0, int((board_size - 1) / 2)])

    return positions


# PLAYERS FUNCTIONS

def add_figure(player, board, figures):
    if player == 'A':
        if board[0][int((board_size + 1) / 2)] == 'A':
            print('Na štarte už je panáčik hráča A')
        else:
            board[0][int((board_size + 1) / 2)] = 'A'
            figures.append([0, int((board_size - 1) / 2 + 1), 0])

    if player == 'B':
        if board[int(board_size - 1)][int((board_size - 3) / 2)] == 'B':
            print('Na štarte už je panáčik hráča B')
        else:
            board[int(board_size - 1)][int((board_size - 3) / 2)] = 'B'
            figures.append([board_size - 1, int((board_size - 1) / 2 - 1), 0])


def moveFigure(board, player, figure, length, figures, figures_in_house):
    positions = get_positions(current_game)

    current_pos = positions.index([figure[0], figure[1]])
    new_pos = current_pos + length

    oldY = positions[current_pos][0]
    oldX = positions[current_pos][1]

    figure_index = figures.index(figure)

    if new_pos == 32:
        new_pos = 0


    if (32 > new_pos) & player == 'A':
        y = positions[new_pos][0]
        x = positions[new_pos][1]
        board[y][x] = str(player)
        board[oldY][oldX] = '*'
        figures[figure_index] = [y, x, 0]

    if (32 < new_pos < 32 + (board_size - 3) / 2) & (player == 'A'):
        board[new_pos - 31][int((board_size - 1) / 2)] = 'A'
        board[oldY][oldX] = '*'
        figures[figure_index][2] = 1
        figures_in_house += 1

    if (32 < new_pos < 32 + (board_size - 3) / 2) & (player == 'B'):
        new_pos = new_pos - current_pos - (32 - current_pos)
        y = positions[new_pos][0]
        x = positions[new_pos][1]
        board[y][x] = str(player)
        board[oldY][oldX] = '*'
        figures[figure_index] = [y, x]

    if (15 < new_pos < 15 + (board_size - 3) / 2) & (player == 'B'):
        board[board_size - new_pos + 14][int((board_size - 1) / 2)] = 'B'
        board[oldY][oldX] = '*'
        figures[figure_index][2] = 1
        figures_in_house += 1



# GAME

board_size = int(input("Zadaj velkost šachovnice"))
current_game = create_game(board_size)

start_game(current_game)

