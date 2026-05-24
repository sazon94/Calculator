from Scanner import Scanner
from Frc import Frc

def main():
    print('Enter number: ')
    a = Scanner.get_type_num(input())


    while a == 'Is not correct number, try again!':
        print('Is not correct number, try again!')
        print('Enter number: ')
        a = Scanner.get_type_num(input())

    if type(a) in (int, float):
        a = Frc.to_frc(a)

    result = a

    print('Press enter to finish typing')


    while True:


        while True:
            print('Enter operation (+, -, *, /): ')
            b = input().strip()

            if b == '':
                break

            elif any(x not in '+-*/' for x in b) or len(b) != 1:
                print('Your operation is not correct!')
                continue

            else:
                break


        operation = b

        if operation == '':
            break

        print('Enter number: ')
        c = Scanner.get_type_num(input())


        while c == 'Is not correct number, try again!':
            print('Is not correct number, try again!')
            print('Enter number: ')
            c = Scanner.get_type_num(input())

        if type(c) in (int, float):
            c = Frc.to_frc(c)

        if operation == '+':
            result += c

        elif operation == '-':
            result -= c

        elif operation == '*':
            result *= c

        elif operation == '/':
            result /= c

    return result


if __name__ == '__main__':
    print(main())