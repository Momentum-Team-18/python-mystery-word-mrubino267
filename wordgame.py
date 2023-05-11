import random


words = ['shenanigans', 'football', 'bamboozle', 'goblin', 'malarkey',
        'whippersnapper', 'microscope', 'lollygag']
# next we need to pick a random word from the list of words

random_word = random.choice(words)
# random_word is variable we assign the random word to


print('***Word Guessing Game***')

user_guesses = ''
# create a variable to append all the guesses a user makes/as initial value set it to single quotes
chances = 8

while chances > 0:
    wrong_guesses = 0
    for character in random_word:
        if character in user_guesses:
            print(f"Correct guess: {character}")
        else:
            wrong_guesses += 1
            print('_')

    if wrong_guesses == 0:
        print("Correct")
        print(f"Word : {random_word}")
        break
    guess = input('Make a guess: ')
    user_guesses += guess

    if guess not in random_word:
        chances -= 1
        print(f"Wrong. You have {chances} more chances")

    if chances == 0:
        print("You're a wicked big Loosah")

    # for each character in the random word that was picked we need to check w. user guesses


# as long as the number of chances is greater than 0 user plays game, inside lopp create varfor wrong guesses
