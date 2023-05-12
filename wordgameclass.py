import random


def play_game(filename):
    with open(filename) as file:
        word_list = file.read().split()
    random_word = random.choice(word_list)
    print('Do you want to play a game?')
    word_list= {}
    print(random_word)
    display = []
    for character in random_word:
        display.append('_')
    print(display)
    #5/6 open as long as you need open with/open structure indent

    # random_word is variable we assign the random word to
    
    
    user_guesses = ''
    # create a variable to append all the guesses a user makes/as initial value set it to single quotes
    chances = 8
    

    while chances > 0 and '_' not in display:
        guess = input('Make a guess: ')
        user_guesses += guess
        if guess not in random_word:
            chances -= 1
            print(f"Wrong. You have {chances} more chances")
        else:
            for i in range(len(random_word)):
                if guess == random_word[i]:
                    display[i] = guess
            print(display)



    if chances == 0:
        print(f"You're a wicked big Loozah. Answer: {random_word} ")
    # else:
    #     print("You're a winnah")

    # for each character in the random word that was picked we need to check w. user guesses


# as long as the number of chances is greater than 0 user plays game, inside lopp create varfor wrong guesses

if __name__ == "__main__":
    play_game("words.txt")
