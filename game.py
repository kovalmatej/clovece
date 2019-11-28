n = int(input("Zadaj velkost šachovnice"))

def generateBoard(n):
    gameBoard = [[' '] * n for i in range(n)] # Vytvorí prázdne miesto pre všetky prvky matice
    return gameBoard

def drawBoard(gameBoard):
    for row in gameBoard:
        print(' '.join([element for element in row])) # Vypíše všetky elementy v riadku a spojí ich medzerou

drawBoard(generateBoard(n))