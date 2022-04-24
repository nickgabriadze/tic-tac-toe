import pygame

pygame.init()

WIDTH, HEIGHT = 720, 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
TicTacToeBoard = pygame.image.load("TicTacToeBoard.png")
TicTacToeBoard = pygame.transform.scale(TicTacToeBoard, (350, 350))
X = pygame.image.load("XO/X.png")
OurO = pygame.image.load("XO/O.png")
startColour = (43, 44, 45)
playAgain = pygame.USEREVENT + 2
gameWindow.fill(startColour)
pygame.display.update()
placementCounterForXO = 0

BoxO = [False, False, False, False, False, False, False, False, False]
BoxX = [False, False, False, False, False, False, False, False, False]
Board = [False, False, False, False, False, False, False, False, False]


def welcomeScreen():
    gameWindow.fill(startColour)
    font = pygame.font.Font('Fonts/Poppins/Poppins-Regular.ttf', 45)
    ruleFont = pygame.font.Font('Fonts/Poppins/Poppins-Medium.ttf', 25)
    pressSFont = pygame.font.Font('Fonts/Poppins/Poppins-SemiBold.ttf', 30)
    welcomeText = font.render("Welcome to Tic Tac Toe", False, (229, 184, 11))
    rulesText = ruleFont.render("Only rule here: Tic Tac Toe The Shit Out Of It", False, (229, 184, 11))
    pressS = pressSFont.render("Press 'S' to start playing", False, (229, 184, 20))
    gameWindow.blit(rulesText, (WIDTH // 2 - 270, HEIGHT // 2 + 240))
    gameWindow.blit(welcomeText, (WIDTH // 2 - 260, HEIGHT // 2 - 260))
    gameWindow.blit(TicTacToeBoard, (WIDTH // 2 - 170, HEIGHT // 2 - 190))
    gameWindow.blit(pressS, (WIDTH // 2 - 180, HEIGHT // 2 + 170))
    pygame.display.update()


def playScreen():
    pygame.display.set_caption("X starts the game!")
    gameWindow.fill((0, 0, 10))
    borderX = WIDTH // 3
    borderY = HEIGHT // 3
    for i in range(0, 4):
        if i % 2 == 0:
            BORDER = pygame.Rect(borderX, 0, 10, HEIGHT)
            pygame.draw.rect(gameWindow, (190, 0, 50), BORDER)
            borderX = borderX + WIDTH // 3
        else:
            BORDER = pygame.Rect(0, borderY, WIDTH, 10)
            pygame.draw.rect(gameWindow, (190, 0, 50), BORDER)
            borderY = borderY + HEIGHT // 3

    pygame.display.update()
    pass


def placeXO(mousePos, XorO):
    if XorO % 2 == 0:
        # For X
        # First row
        pygame.display.set_caption("O's Turn")
        if 0 < mousePos.__getitem__(0) < 240 and mousePos.__getitem__(1) < 200:
            if not Board[0]:
                gameWindow.blit(X, (0, 0))
                pygame.display.update()
                BoxX[0] = True
                Board[0] = True
        elif 240 < mousePos.__getitem__(0) < 480 and mousePos.__getitem__(1) < 200:
            if not Board[1]:
                gameWindow.blit(X, (240, 0))
                pygame.display.update()
                BoxX[1] = True
                Board[1] = True
        elif 480 < mousePos.__getitem__(0) < 720 and mousePos.__getitem__(1) < 200:
            if not Board[2]:
                gameWindow.blit(X, (480, 0))
                pygame.display.update()
                BoxX[2] = True
                Board[2] = True

            # Second  row
        if 0 < mousePos.__getitem__(0) < 240 and 200 < mousePos.__getitem__(1) < 400:
            if not Board[3]:
                gameWindow.blit(X, (0, 200))
                pygame.display.update()
                BoxX[3] = True
                Board[3] = True
        elif 240 < mousePos.__getitem__(0) < 480 and 200 < mousePos.__getitem__(1) < 400:
            if not Board[4]:
                gameWindow.blit(X, (240, 200))
                pygame.display.update()
                BoxX[4] = True
                Board[4] = True
        elif 480 < mousePos.__getitem__(0) < 720 and 200 < mousePos.__getitem__(1) < 400:
            if not Board[5]:
                gameWindow.blit(X, (480, 200))
                pygame.display.update()
                BoxX[5] = True
                Board[5] = True
        # Third row
        if 0 < mousePos.__getitem__(0) < 240 and 400 < mousePos.__getitem__(1) < 600:
            if not Board[6]:
                gameWindow.blit(X, (0, 400))
                pygame.display.update()
                BoxX[6] = True
                Board[6] = True
        elif 240 < mousePos.__getitem__(0) < 480 and 400 < mousePos.__getitem__(1) < 600:
            if not Board[7]:
                gameWindow.blit(X, (240, 400))
                pygame.display.update()
                BoxX[7] = True
                Board[7] = True
        elif 480 < mousePos.__getitem__(0) < 720 and 400 < mousePos.__getitem__(1) < 600:
            if not Board[8]:
                gameWindow.blit(X, (480, 400))
                pygame.display.update()
                BoxX[8] = True
                Board[8] = True

    else:
        # For O
        # First row
        pygame.display.set_caption("X's Turn")
        if 0 < mousePos.__getitem__(0) < 240 and mousePos.__getitem__(1) < 200:
            if not Board[0]:
                gameWindow.blit(OurO, (0, 0))
                pygame.display.update()
                BoxO[0] = True
                Board[0] = True
        elif 240 < mousePos.__getitem__(0) < 480 and mousePos.__getitem__(1) < 200:
            if not Board[1]:
                gameWindow.blit(OurO, (240, 0))
                pygame.display.update()
                BoxO[1] = True
                Board[1] = True
        elif 480 < mousePos.__getitem__(0) < 720 and mousePos.__getitem__(1) < 200:
            if not Board[2]:
                gameWindow.blit(OurO, (480, 0))
                pygame.display.update()
                BoxO[2] = True
                Board[2] = True

        # Second  row
        if 0 < mousePos.__getitem__(0) < 240 and 200 < mousePos.__getitem__(1) < 400:
            if not Board[3]:
                gameWindow.blit(OurO, (0, 200))
                pygame.display.update()
                BoxO[3] = True
                Board[3] = True
        elif 240 < mousePos.__getitem__(0) < 480 and 200 < mousePos.__getitem__(1) < 400:
            if not Board[4]:
                gameWindow.blit(OurO, (240, 200))
                pygame.display.update()
                BoxO[4] = True
                Board[4] = True
        elif 480 < mousePos.__getitem__(0) < 720 and 200 < mousePos.__getitem__(1) < 400:
            if not Board[5]:
                gameWindow.blit(OurO, (480, 200))
                pygame.display.update()
                BoxO[5] = True
                Board[5] = True
        # Third row
        if 0 < mousePos.__getitem__(0) < 240 and 400 < mousePos.__getitem__(1) < 600:
            if not Board[6]:
                gameWindow.blit(OurO, (0, 400))
                pygame.display.update()
                BoxO[6] = True
                Board[6] = True
        elif 240 < mousePos.__getitem__(0) < 480 and 400 < mousePos.__getitem__(1) < 600:
            if not Board[7]:
                gameWindow.blit(OurO, (240, 400))
                pygame.display.update()
                BoxO[7] = True
                Board[7] = True
        elif 480 < mousePos.__getitem__(0) < 720 and 400 < mousePos.__getitem__(1) < 600:
            if not Board[8]:
                gameWindow.blit(OurO, (480, 400))
                pygame.display.update()
                BoxO[8] = True
                Board[8] = True


def checkForWinner(MainBoard, BoxForX, BoxForO):
    gameOver = False
    font = pygame.font.Font('Fonts/Poppins/Poppins-Medium.ttf', 60)
    if BoxForX[0] and BoxForX[1] and BoxForX[2] \
            or BoxForX[3] and BoxForX[4] and BoxForX[5] \
            or BoxForX[6] and BoxForX[7] and BoxForX[8] \
            or BoxForX[0] and BoxForX[3] and BoxForX[6] \
            or BoxForX[1] and BoxForX[4] and BoxForX[7] \
            or BoxForX[2] and BoxForX[5] and BoxForX[8] \
            or BoxForX[0] and BoxForX[4] and BoxForX[8] \
            or BoxForX[2] and BoxForX[4] and BoxForX[6]:
        pygame.display.set_caption("And there winner is X!")
        result = font.render("X Won!", False, (180, 0, 0))
        gameWindow.blit(result, (WIDTH // 2 - 100, HEIGHT // 2 - 100))
        gameOver = True
        pygame.display.update()

    elif BoxForO[0] and BoxForO[1] and BoxForO[2] \
            or BoxForO[3] and BoxForO[4] and BoxForO[5] \
            or BoxForO[6] and BoxForO[7] and BoxForO[8] \
            or BoxForO[0] and BoxForO[3] and BoxForO[6] \
            or BoxForO[1] and BoxForO[4] and BoxForO[7] \
            or BoxForO[2] and BoxForO[5] and BoxForO[8] \
            or BoxForO[0] and BoxForO[4] and BoxForO[8] \
            or BoxForO[2] and BoxForO[4] and BoxForO[6]:
        pygame.display.set_caption("And there winner is O!")
        result = font.render("O Won!", False, (0, 0, 190))
        gameWindow.blit(result, (WIDTH // 2 - 100, HEIGHT // 2 - 100))
        gameOver = True
        pygame.display.update()

    else:
        if MainBoard[0] and MainBoard[1] and MainBoard[2] and MainBoard[3] \
                and MainBoard[4] and MainBoard[5] and MainBoard[6] and MainBoard[7] \
                and MainBoard[8]:
            pygame.display.set_caption("And It's a Tie!")
            result = font.render("It's a Tie!", False, (229, 184, 11))
            gameWindow.blit(result, (WIDTH // 2 - 120, HEIGHT // 2 - 100))
            gameOver = True
            pygame.display.update()

    if gameOver:
        font = pygame.font.Font('Fonts/Poppins/Poppins-Medium.ttf', 20)
        text = font.render("Press Q to Quit", False, (229, 184, 11))
        gameWindow.blit(text, (WIDTH // 2 - 70, HEIGHT // 2 - 20))
        pygame.display.update()

        pressedKey = pygame.key.get_pressed()
        if pressedKey[pygame.K_q]:
            return True

    return False


def TicTacToe():
    weRun = True
    FPS = 30
    clock = pygame.time.Clock()
    welcomeScreen()
    XorO = 0
    WelcomeScreen = 0
    while weRun:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                weRun = False

            if WelcomeScreen == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    XO = pygame.mouse.get_pos()
                    placeXO(XO, XorO)
                    XorO += 1

        pressedKey = pygame.key.get_pressed()
        if WelcomeScreen == 0:
            if pressedKey[pygame.K_s]:
                playScreen()
                WelcomeScreen += 1

        if checkForWinner(Board, BoxX, BoxO):
            weRun = False


if __name__ == "__main__":
    TicTacToe()
