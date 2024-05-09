from random import randint


def guessing_game():
    number = int(randint(1, 100))

    while True:
        guess = input("Guess the number: ")

        try:
            guess = int(guess)
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too big!")
            else:
                print("You win!")
                break
        except ValueError:
            print("It's not a number!")


if __name__ == '__main__':
    guessing_game()
