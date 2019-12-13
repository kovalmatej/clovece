#TO DO:
#ked mam dvoch panacikov a padla 6 (A/B) tak musim hrat
#niekedy nejde selectnut Bcko
import random


# MAIN GAME FUNCTIONS

def throw_dice():
    return random.randint(1, 6)


def six_throwed(game_board, player, figures, figures_in_house, board_size):
    choice = int(
        input("Padla 6, zadaj 1 ak chceš pridať nového panáčika, ľubovoľnú inú hodnotu ak chceš pohnúť panáčikom."))

    if figures_in_house == len(figures):
        choice = 1
        print("Bola pridaná figurka")

    if choice == 1:
        print("Bola pridaná figurka")
        add_figure(player, game_board, figures, board_size)
    return choice


def game_status(counter):
    throwed_number = throw_dice()

    if counter % 2 == 0:
        print("Na rade je hrac A a hodil cislo: ", throwed_number)
    else:
        print("Na rade je hrac B a hodil cislo: ", throwed_number)
    return throwed_number


def start_game():
    figures1 = []  # Listy pozícií panáčikov a koľko ich je v domčeku z jednotlivých tímov.
    figures2 = []

    winner = ''
    board_size = int(input("Zadaj veľkosť hracej plochy"))
    game_board = generate_board(board_size)

    add_figure('A', game_board, figures1, board_size)
    add_figure('B', game_board, figures2, board_size)

    counter = 0

    draw_board(game_board)
    while winner == '':
        number = game_status(counter)
        y, x, choice = 0, 0, 0
        figures_in_houseA = 0
        figures_in_houseB = 0

        for i in range( len(figures1) ):
            if figures1[i][2] == 1:
                figures_in_houseA += 1
        for i in range(len(figures2)):
            if figures2[i][2] == 1:
                figures_in_houseB += 1

        if counter % 2 == 0:
            make_move(game_board, 'A', number, figures1, figures2, figures_in_houseA, y, x, choice, board_size)

        if counter % 2 == 1:
            make_move(game_board, 'B', number, figures2, figures1, figures_in_houseB, y, x, choice, board_size)

        print(figures1, " a ", figures2)

        counter += 1

        if figures_in_houseA == 4:
            winner = 'A'
        elif figures_in_houseB == 4:
            winner = 'B'

        draw_board(game_board)


# CHECKING FUNCTIONS

def check_position(board, player, position):  # Zistí či je voľná štartovacia pozícia pre jednotlivého hráča
    if board[position[0]][position[1]] == player:
        return False
    return True


# GAME BOARD FUNCTIONS

# N je veľkosť hracej plochy
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
    for i in range(len(game_board)):
        if i < 10:
            print(i, end=" ")
        else:
            print(i - 10, end=" ")
    print("")

    a = 0
    for row in game_board:
        if a < 10:
            print(a, "", end=" ")
        else:
            print(a - 10, "", end=" ")
        a += 1
        print(' '.join([element for element in row]))  # Vypíše všetky elementy v riadku a spojí ich medzerou


# Uloží pozície hracej plochy do listu za sebou
def get_positions(game_board, board_size):
    positions = []

    for i in range(int((board_size - 1) / 2)):
        for j in range(int((board_size - 1) / 2) + 1, board_size):
            if (game_board[i][j] != ' ') & (game_board[i][j] != 'D') & (game_board[i][j] != 'X'):
                positions.append([i, j])

    positions.append([int((board_size - 1) / 2), board_size - 1])

    for i in range(int((board_size - 1) / 2) + 1, board_size - 1):
        for j in range(board_size - 1, int((board_size - 1) / 2), -1):

            if (game_board[i][j] != ' ') & (game_board[i][j] != 'D') & (game_board[i][j] != 'X'):
                positions.append([i, j])

    positions.append([board_size - 1, int((board_size - 1) / 2) + 1])

    for i in range(board_size - 1, int((board_size - 1) / 2), -1):
        for j in range(int((board_size - 1) / 2), 0, -1):
            if (game_board[i][j] != ' ') & (game_board[i][j] != 'D') & (game_board[i][j] != 'X'):
                positions.append([i, j])

    positions.append([int((board_size - 1) / 2) + 1, 0])

    for i in range(int((board_size - 1) / 2), -1, -1):
        for j in range(0, int((board_size - 1) / 2)):
            if (game_board[i][j] != ' ') & (game_board[i][j] != 'D') & (game_board[i][j] != 'X'):
                positions.append([i, j])

    positions.append([0, int((board_size - 1) / 2)])

    return positions



# Skontroluje či pozícia na ktorú sa ide panáčik pohnúť je validná
def check_moving_position(game_board, player, figure, length, board_size):
    if (figure[1] == 0) & (figure[0] == 0):
        return False

    positions = get_positions(game_board, board_size)

    if [figure[0], figure[1]] in positions:  # Načíta pozíciu na ktorej sa nachádza panáčik
        current_pos = positions.index([figure[0], figure[1]])
    else:
        return False

    new_pos = current_pos + length  # Zistí súradnice novej pozície
    if new_pos >= (board_size - 1) * 4:
        new_pos -= (board_size - 1) * 4

    if (game_board[positions[new_pos][0]][positions[new_pos][1]]) == player:
        return False

    return True


# PLAYERS FUNCTIONS

def add_figure(player, board, figures, board_size):
    # Otestuje či je voľná štartovacia plocha a ak áno tak pridá figúrku
    if (player == "A") & (check_position(board, player, [0, int((board_size + 1) / 2)])):
        figures.append([0, int((board_size - 1) / 2 + 1), 0])
        board[0][int((board_size - 1) / 2 + 1)] = player
    elif (player == "B") & (check_position(board, player, [board_size - 1, int((board_size - 1) / 2 - 1)])):
        figures.append([board_size - 1, int((board_size - 1) / 2 - 1), 0])
        board[board_size - 1][int((board_size - 1) / 2 - 1)] = player


# figure - je pozícia figúrky ktorú treba zmazať a figure_index je jej index v liste
def delete_figure(player, board, figures, figures2, figure, old_pos, figure_index):
    board[figure[0]][figure[1]] = player
    board[old_pos[0]][old_pos[1]] = '*'

    if player == 'B':
        figures[figure_index] = [figure[0], figure[1], 0]
        figures2.remove(figure)
    else:
        figures2[figure_index] = [figure[0], figure[1], 0]
        figures.remove(figure)


# y, x sú nové pozície a choice je premenná, ktorá uchovavá akú možnosť si užívateľ zvolil pri hodení 6
def make_move(board, player, number, figures1, figures2, figures_in_house, y, x, choice, board_size):
    if player == 'A':
        start_pos = [0, int((board_size + 1) / 2)]
    else:
        start_pos = [board_size - 1, int((board_size - 1) / 2 - 1)]

    if (number == 6) & (len(figures1) < (board_size - 3) / 2) & (
            check_position(board, player, [start_pos[0], start_pos[1]])):
        choice = six_throwed(board, player, figures1, figures_in_house, board_size)
    if ((len(figures1) == 1) | (len(figures1) - figures_in_house) == 1) & (figures_in_house != len(figures1)) & (
            choice != 1):
        lonely_figure = 0

        for i in range(len(figures1)):
            if figures1[i][2] == 0:
                lonely_figure = i
                break

        move_figure(board, player, figures1[lonely_figure], number, figures1, figures2, board_size)

    elif (len(figures1) != 1) & (len(figures1) - figures_in_house > 1) & (choice != 1):
        while (not (check_moving_position(board, player, [y, x, 0], number, board_size))) | (
                not (([y, x, 0]) in figures1)):
            x = int(input("Zadaj X súradnicu panáčika, ktorým chceš pohnúť."))
            y = int(input("Zadaj Y súradnicu panáčika, ktorým chceš pohnúť."))
        figure = figures1.index([y, x, 0])

        move_figure(board, player, figures1[figure], number, figures1, figures2, board_size)


def move_figure(board, player, figure, length, figures, figures2, board_size):
    if figure[2] == 1:  # Ak selektnutý panáčik už je v domčeku
        return

    positions = get_positions(board, board_size)
    y, x = 0, 0

    old_index = positions.index([figure[0], figure[1]])
    print("Old index je: ", old_index, " a length je ", length)
    new_index = old_index + length
    old_pos = [positions[old_index][0], positions[old_index][1]]

    figure_index = figures.index(figure)

    if (new_index == (board_size - 1) * 4) & (player == 'B') | ((player == 'A') & (old_index > ((board_size - 1) * 4) - 6)):
        new_index = 0
    print("index je:", new_index)
    if new_index < (board_size - 1) * 4:
        y = positions[new_index][0]
        x = positions[new_index][1]

    if (board[y][x] == 'A') & (player == 'B'):
        delete_figure('B', board, figures, figures2, [y, x, 0], old_pos, figure_index)
    elif (board[y][x] == 'B') & (player == 'A'):
        delete_figure('A', board, figures, figures2, [y, x, 0], old_pos, figure_index)
    else:

        if (board_size - 1) * 4 > new_index:
            if (player == 'B') & (((board_size - 1) * 2) - 1 < new_index < ((board_size - 1) * 2 ) + (board_size - 3) / 2) & (old_index <= ((board_size - 1) * 2) - 1):
                board[board_size - new_index + ((board_size - 1) * 2) - 2][int((board_size - 1) / 2)] = 'B'
                board[old_pos[0]][old_pos[1]] = '*'
                figures[figure_index] = [board_size - new_index + ((board_size - 1) * 2) - 2, int((board_size - 1) / 2), 1]
            else:
                if not( (player == "B") & (new_index > (board_size * 2) + 1) & ((((board_size - 1) * 2) - 1) > old_index > (board_size + (board_size - 3)/ 2))):
                    board[old_pos[0]][old_pos[1]] = '*'
                    board[y][x] = player
                    figures[figure_index] = [y, x, 0]

        if ((board_size - 1) * 4 <= new_index < (board_size - 1) * 4 + (board_size - 3) / 2) & (player == 'A'):
            board[new_index - ((board_size - 1) * 4) + 1][int((board_size - 1) / 2)] = 'A'
            board[old_pos[0]][old_pos[1]] = '*'
            figures[figure_index] = [new_index - ((board_size - 1) * 4) + 1, int((board_size - 1) / 2), 1]

        if ((board_size - 1) * 4 <= new_index < (board_size - 1) * 4 + 6) & (player == 'B'):
            new_index = new_index - old_index - ((board_size - 1) * 4 - old_index)
            y = positions[new_index][0]
            x = positions[new_index][1]

            board[y][x] = player
            board[old_pos[0]][old_pos[1]] = '*'

            figures[figure_index] = [y, x, 0]







# GAME

start_game()
