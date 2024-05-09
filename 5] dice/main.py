from random import randint

dice = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")


def roll_the_dice(input_dice):
    for cube in dice:
        if cube in input_dice:
            try:
                number_of_rolls, modifier = input_dice.split(cube)
            except ValueError:
                return "Wrong Dice"
            type_of_dice = cube[1:]
            break
    else:
        return "Wrong dice"

    if number_of_rolls == "":
        number_of_rolls = 1

    if modifier == "":
        modifier = 0

    number_of_rolls, type_of_dice, modifier = map(int, [number_of_rolls, type_of_dice, modifier])

    # dice_sum = 0
    # for i in range(number_of_rolls):
    #     dice_sum += randint(1, type_of_dice)
    #
    # calculation1 = dice_sum + modifier
    # print(f"Calculation1: {calculation1}")

    calculation = sum([randint(1, type_of_dice) for i in range(number_of_rolls)]) + modifier

    return f"The Result of the dice roll {input_dice} is {calculation}"


if __name__ == "__main__":
    print(roll_the_dice("2D6+4"))
