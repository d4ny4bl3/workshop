def answer():
    posibble_answer = ["too small", "too big", "you win"]
    while True:
        user_answer = input("Is this a correct guess?: ")
        user_answer.lower()
        if user_answer in posibble_answer:
            break
        else:
            print("You can only write 'too big', too small', 'you win')")
    return user_answer


def guessing_game():
    print("Think about a number from 0 to 100 and let me guess it!")
    print("You can only write 'too big', too small', 'you win')")
    min_num = 0
    max_num = 1000
    user_answer = ""
    while True:
        guess = int((max_num - min_num) / 2) + min_num
        print(f"Guessing: {guess}")
        user_answer = answer()
        if user_answer == "too big":
            max_num = guess
        elif user_answer == "too small":
            min_num = guess
        elif user_answer == "you win":
            print("I won!")
            break


if __name__ == "__main__":
    guessing_game()
