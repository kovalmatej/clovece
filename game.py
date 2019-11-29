board_size = int(input("Zadaj velkost šachovnice"))


def generate_board(n):
    game_board = [[' '] * n for i in range(n)]  # Vytvorí prázdne miesto pre všetky prvky matice

    for i in range(n):
        for j in range(n):
            # 1. časť = Selektuje všetky prvky vo vnútornom "krížiku", kde ramená sú dĺžky 3
            if (((n - 3) / 2 <= j <= (n + 1) / 2) & ((j != (n - 1) / 2) & (i != (n - 1) / 2))) | (
            # 2. časť = Vyhodí vnútro, kde budú domčeky
                    (i == (n - 1) / 2) & ((j == 0) | (j == n - 1))) | (
            # Aby horná podmienka nevyhodila konce, tak sa určia vínimky v strede obidvoch cyklov ak je jeden...
                    (j == (n - 1) / 2) & ((i == 0) | (i == n - 1))):  # ...z nich na konci alebo na začiatku
                game_board[i][j] = '*'
                game_board[j][i] = '*'
            if (j == (n - 1) / 2) & (i != n-1):
                game_board[i][j] = 'D'
                game_board[j][i] = 'D'

    game_board[int((n - 1) / 2)][int((n - 1) / 2)] = 'X'
    return game_board


def draw_board(game_board):
    for row in game_board:
        print(' '.join([element for element in row]))  # Vypíše všetky elementy v riadku a spojí ich medzerou


draw_board(generate_board(board_size))
