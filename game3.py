import random


def play_game(filename):
    with open(filename) as file:
        word_list = file.read().split()
    random_word = random.choice(word_list)
    blanks = [' _ '] * len(random_word)
    print('Do you want to play a game?')

    word_list = {}
    print(random_word)

    # display = []
    # for character in random_word:
    #     display.append('-')
    # print(display)

character = ('random_word'[0:])
user_guesses = ''
guesses = 5

while guesses > 0:
    wrong_guesses = 0
    for character in user_guesses:
        if character in random_word:
            print(f"Correct guess: {character}")
    else:
        wrong_guesses += 1
        print('_')

    if wrong_guesses == 0:
        print("Correct")
        print(f"Word : {random_word}")
        break
    guess = input('Guess a letter: ')
    user_guesses += guess

    if guess not in random_word:
        guesses -= 1
        print(f"Wrong. You have {guesses} more chances")

    if guesses == 0:
        print("You're a wicked big Loosah")

    if __name__ == "__main__":
        play_game("words.txt")
