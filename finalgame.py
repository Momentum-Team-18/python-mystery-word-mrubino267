import random


def play_game():
    with open('words.txt') as f:
        text = f.read()
    text_full = text.split()
    random_word = random.choice(text_full)

    correct_letters = []

    print("Welcome to Mystery Word, your word has: " +
        str(len(random_word)) + " characters.")

    for guess in random_word:
        correct_letters.append('_')

    guesses = 6
    while guesses > 0:
        guess = input("Please enter one letter: " + str(correct_letters) + " ")
        if guess in random_word:
            for i in range(len(random_word)):
                if guess == random_word[i]:
                    correct_letters[i] = guess
                    print("That letter is correct 🕺.")
        else:
            guesses -= 1
            print("👎🏻, you have " + str(guesses) + " left.")
    else:
        guesses = 0
        print("🛑 You lost, the word was: " + str(random_word))


if __name__ == "__main__":
    play_game()
