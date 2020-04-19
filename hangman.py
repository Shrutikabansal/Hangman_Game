import random
#from words import get_random_word
 
def play_again():
    answer = input('Would you like to play again? yes/no').lower()
    if answer == 'y' or answer =='yes':
        play_game()
    else:
        return   #pass

def get_word():
    words = ['aaa','cat', 'dog', 'python', 'monkey', 'snake', 'random', 'house', 'office']
    return random.choice(words)

def play_game():
    word = get_word()
    letters_guessed = []
    tries = 10
    guessed = False

    print('The word of', len(word), 'letters.')
    print(len(word) * '*')
    while guessed == False and tries > 0:
        print('You are remaining with ' + str(tries) + ' tries')
        guess = input('Please enter one letter or the full word.').lower()
        #1 - user inputs a letter
        if len(guess) == 1:
            if ord(guess)<97 and ord(guess)>122:
                print('This letter is not allowed.')
            elif guess in letters_guessed:
                print('This letter already guessed.')
            elif guess not in word:
                print('This letter does not belong to this word')
                letters_guessed.append(guess)
                tries -=1
            elif guess in word:
                print('Yehhh...., This letter exist in this word.')
                letters_guessed.append(guess)
            else:
                print('No idea why we get this message, There is something wrong')

        #2 - user inputs the full word
        elif len(guess) == len(word):
            if guess == word:
                print('Yehhh..., Finally you have guessed the word!')
                guessed = True
            else:
                print('Oops.., Wrong guess !! Better Luck next time')
                tries -= 1

        #3 - user inputs letters where the total number of letters =/= total number of letters in the word.  
        else:
            print('The length of your guess is not the same as the length of the word we\'re looking for.')

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '*'
            print(status)

        if status == word:
            print('Yehhh..., Finally you have guessed the word!')
            guessed = True
        elif tries == 0:
            print('Sorry, but You have run out of guesses and you haven\'t guessed the word.')

    play_again()

play_game()