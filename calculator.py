from frc import Frc
from scanner import Scanner


def calc(mathematical_example: str):
    tokens = mathematical_example.split()

    # Converting numbers from a string data type
    # to a Frc class type to simplify mathematical operations

    for i in range(0, len(tokens), 2):
        num = Scanner.get_type_num(tokens[i])        # int, float or Frc
        num = Frc.to_frc(num)
        tokens[i] = num


    # Block of mathematical operations with correct mathematical order

    while '*' in tokens or '/' in tokens:

        if '*' in tokens:
            mul_index = tokens.index('*')
        else:
            mul_index = float('inf')

        if '/' in tokens:
            div_index = tokens.index('/')
        else:
            div_index = float('inf')

        # Performing multiplication/division in order from left to right

        if mul_index < div_index:
            result = tokens[mul_index - 1] * tokens[mul_index + 1]
            tokens[mul_index - 1 : mul_index + 2] = [result]
            continue

        elif div_index < mul_index:
            result = tokens[div_index - 1] / tokens[div_index + 1]
            tokens[div_index - 1 : div_index + 2] = [result]
            continue


    while '+' in tokens or '-' in tokens:

        if '+' in tokens:
            add_index = tokens.index('+')
        else:
            add_index = float('inf')

        if '-' in tokens:
            sub_index = tokens.index('-')
        else:
            sub_index = float('inf')

        # Performing addition/subtraction in order from left to right

        if add_index < sub_index:
            result = tokens[add_index - 1] + tokens[add_index + 1]
            tokens[add_index - 1 : add_index + 2] = [result]
            continue

        elif sub_index < add_index:
            result = tokens[sub_index - 1] - tokens[sub_index + 1]
            tokens[sub_index - 1 : sub_index + 2] = [result]
            continue


    return tokens[0]


def correct_opening_of_brackets(mathematical_example: str):

    tokens = mathematical_example.split()

    while '(' in tokens:

        index_closing = tokens.index(')')
        all_index_opening = [i for i in range(len(tokens)) if tokens[i] == '(' and i < index_closing]
        index_opening = max(all_index_opening)

        new_math_example = [tokens[i] for i in range(index_opening + 1, index_closing)]

        new_string = ' '.join(new_math_example)

        result = calc(new_string)

        tokens[index_opening] = str(result)

        for i in range(index_closing - index_opening):
            del tokens[index_opening + 1]

        continue

    new_mathematical_string = ' '.join(tokens)

    return new_mathematical_string


def main():
    print('Enter a mathematical example: ')
    math_example = input()

    # Check correct mathematical example

    if not(Scanner._check_correct_math_operation(math_example))\
       or not(Scanner._check_correct_placement_of_parentheses(math_example)):

        print('You have entered an incorrect mathematical example!')

    else:

        try:
            result = calc(correct_opening_of_brackets(math_example))
            print(result)

        except ZeroDivisionError:
            print('Dividing by zero is a mistake in mathematics!')


main()