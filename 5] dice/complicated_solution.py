from random import randint

dice = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")


def format_dice(dice):
    dice_split = dice.split("D")
    if len(dice_split) != 2:
        print("Wrong format of dice")
    number_of_rolls, type_and_modifier = dice_split

    if not number_of_rolls:
        number_of_rolls = 1

    if "+" in type_and_modifier:
        x = type_and_modifier.split("+")
        type_of_dice, modifier = map(int, x)   # type_of_dice, modifier = x
        print(f"+: {number_of_rolls, type_of_dice, modifier}")
        print(f"Type +: number_of_rolls", type(type_of_dice))
        print(f"Type +: type_of_dice", type(modifier))
        print(f"Type +: modifier", type(modifier))
        return number_of_rolls, type_of_dice, modifier
    elif "-" in type_and_modifier:
        x = type_and_modifier.split("-")
        type_of_dice, modifier = map(int, x)
        print(f"-: {number_of_rolls, type_of_dice, modifier}")
        print(f"Type -: number_of_rolls", type(type_of_dice))
        print(f"Type -: type_of_dice", type(modifier))
        print(f"Type -: modifier", type(modifier))
        return number_of_rolls, type_of_dice, -modifier

    print(f"Type d6 number:", type(number_of_rolls))
    print(f"Type d6 type:", type(type_and_modifier))

    return number_of_rolls, type_and_modifier, None


def roll_the_dice():
    pass


if __name__ == "__main__":
    roll = input("Enter a roll the dice: ").upper()
    print(format_dice(roll))
