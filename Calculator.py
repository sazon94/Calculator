from Frc import Frc
from Scanner import Scanner


def calc(a: str):
    b = a.split()


    for i in range(0, len(b), 2):
        num = Scanner.get_type_num(b[i])

        if type(num) in (int, float):
            num = Frc.to_frc(num)

        b[i] = num


    while '*' in b or '/' in b:
        if '*' in b:
            i_1 = b.index('*')
        else:
            i_1 = 99999999
        if '/' in b:
            i_2 = b.index('/')
        else:
            i_2 = 99999999


        if i_1 < i_2:
            result = b[i_1 - 1] * b[i_1 + 1]
            b[i_1] = result
            b.pop(i_1 - 1)
            b.pop(i_1)
            continue

        elif i_2 < i_1:
            result = b[i_2 - 1] / b[i_2 + 1]
            b[i_2] = result
            b.pop(i_2 - 1)
            b.pop(i_2)
            continue

    while '+' in b or '-' in b:
        if '+' in b:
            i_1 = b.index('+')
        else:
            i_1 = 10 ** 10
        if '-' in b:
            i_2 = b.index('-')
        else:
            i_2 = 10 ** 10


        if i_1 < i_2:
            result = b[i_1 - 1] + b[i_1 + 1]
            b[i_1] = result
            b.pop(i_1 - 1)
            b.pop(i_1)
            continue

        elif i_2 < i_1:
            result = b[i_2 - 1] - b[i_2 + 1]
            b[i_2] = result
            b.pop(i_2 - 1)
            b.pop(i_2)
            continue

    return b[0]


def main():
    print('Enter a mathematical example: ')
    math_example = input()

    if not(Scanner._check_correct_math_operation(math_example)):
        print('You have entered an incorrect mathematical example!')

    else:
        return calc(math_example)


print(main())