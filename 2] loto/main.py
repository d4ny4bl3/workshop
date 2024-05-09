from random import shuffle


def user_guess():
    user_guess = []
    order = 1
    while len(user_guess) != 6:
        try:
            num = int(input(f"Enter {order}. number: "))
            if num in user_guess:
                print("You entered the same number!")
                # user_guess = sorted(user_guess)
                print(f"Your numbers are currently: {tuple(sorted(user_guess))}")
            elif num < 1 or num > 49:
                print("Enter a number between 1-49")
            else:
                user_guess.append(num)
                order += 1
        except ValueError:
            print("Must entered a number!")
    return user_guess


def lotto_numbers():
    numbers = [i for i in range(1, 50)]
    shuffle(numbers)
    numbers = numbers[:6]
    return numbers


def format_numbers(numbers):
    print(", ".join(str(i) for i in sorted(numbers)))


def lotto():
    matched_numbers = []
    count = 0
    user_numbers = user_guess()
    lotto_num = lotto_numbers()
    print("\nYour numbers:")
    format_numbers(user_numbers)
    print("Lotto numbers: ")
    format_numbers(lotto_num)
    for i in user_numbers:
        if i in lotto_num:
            count += 1
            matched_numbers.append(i)

    if count >= 1:
        print(f"Matched numbers: ")
        format_numbers(matched_numbers)
    if count == 1:
        print(f"You guessed {count} number!")
    else:
        print(f"You guessed {count} numbers!")


if __name__ == '__main__':
    lotto()
