import pygame
import random

pygame.init()
game_height = 500
gameWidth = 1500
game = pygame.display.set_mode((gameWidth, game_height))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (102, 255, 255)

btn_font = pygame.font.SysFont("arial", 20)
guess_font = pygame.font.SysFont("arial", 24)
lost_font = pygame.font.SysFont('arial', 45)
word = ''
buttons = []
#print(len(buttons))
guessed = []
hangmanPics = [
    pygame.image.load("hangman0.png"),
    pygame.image.load('hangman1.png'),
    pygame.image.load('hangman2.png'),
    pygame.image.load('hangman3.png'),
    pygame.image.load('hangman4.png'),
    pygame.image.load('hangman5.png'),
    pygame.image.load('hangman6.png')]

chances = 0


def redraw_game_gamedow():
    global guessed
    global hangmanPics
    global chances
    game.fill(LIGHT_BLUE)
    # Buttons
    #print(len(buttons))
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(
                game, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
            pygame.draw.circle(
                game, buttons[i][0], (buttons[i][1],buttons[i][2]),buttons[i][3])
            label = btn_font.render(chr(buttons[i][5]), 1, BLACK)
            game.blit(label,
                     (buttons[i][1] - (label.get_width() / 2),
                      buttons[i][2] - (label.get_height() / 2)))

    spaced = spacedOut(word, guessed)
    label1 = guess_font.render(spaced, 1, BLACK)
    rect = label1.get_rect()
    length = rect[2]

    game.blit(label1, (gameWidth / 2 - length / 2, 400))

    pic = hangmanPics[chances]
    game.blit(pic, (gameWidth / 2 - pic.get_width() / 2 + 20, 150))
    pygame.display.update()


def randomWord():
    file = open('words.txt')
    f = file.readlines()
    i = random.randrange(0, len(f) - 1)

    return f[i][:-1]


def hang(guess):
    global word
    if guess.lower() not in word.lower():
        return True
    else:
        return False


def spacedOut(word, guessed=[]):
    spacedWord = ''
    guessedLetters = guessed
    for x in range(len(word)):
        if word[x] != ' ':
            spacedWord += '_ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i]:
                    spacedWord = spacedWord[:-2]
                    spacedWord += word[x].upper() + ' '
        elif word[x] == ' ':
            spacedWord += ' '
    return spacedWord


def buttonHit(x, y):
    for i in range(len(buttons)):
        if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
            if y < buttons[i][2] + 20 and y > buttons[i][2] - 20:
                return buttons[i][5]
    return None


def end(winner=False):
    global chances
    lostTxt = 'Soory! you lost the game \n for continue press any key'
    gameTxt = 'Winner!!! \n for continue press any key '
    redraw_game_gamedow()
    pygame.time.delay(1000)
    game.fill(LIGHT_BLUE)

    if winner:
        label = lost_font.render(gameTxt, 1, BLACK)
    else:
        label = lost_font.render(lostTxt, 1, BLACK)

    wordTxt = lost_font.render(word.upper(), 1, BLACK)
    wordWas = lost_font.render('The phrase was: ', 1, BLACK)

    game.blit(wordTxt, (gameWidth / 2 - wordTxt.get_width() / 2, 295))
    game.blit(wordWas, (gameWidth / 2 - wordWas.get_width() / 2, 245))
    game.blit(label, (gameWidth / 2 - label.get_width() / 2, 140))
    pygame.display.update()
    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                again = False
    reset()


def reset():
    global chances
    global guessed
    global buttons
    global word
    for i in range(len(buttons)):
        buttons[i][4] = True

    chances = 0
    guessed = []
    word = randomWord()



increase = round(gameWidth/13)
for i in range(26):
    if i < 13:
        y = 40
        x = 25 + (increase * i)
    else:
        x = 25 + (increase * (i - 13))
        y = 85
    buttons.append([GREEN, x, y, 20, True, 65 + i])
    # buttons.append([color, x_pos, y_pos, radius, visible, char])

word = randomWord()
playing_game = True


while playing_game:
    redraw_game_gamedow()
    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing_game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playing_game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pos()
            letter = buttonHit(clickPos[0], clickPos[1])
            if letter is not None:
                guessed.append(chr(letter))
                buttons[letter - 65][4] = False
                if hang(chr(letter)):
                    if chances != 5:
                        chances += 1
                    else:
                        end()
                else:
                    print(spacedOut(word, guessed))
                    if spacedOut(word, guessed).count('_') == 0:
                        end(True)

pygame.quit()