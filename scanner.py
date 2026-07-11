from frc import Frc
from reduction import Reduction


class Scanner():


    @staticmethod
    def _check_correct_num(a: str):

        number = a
        alf = '0123456789-/.,'
        integer = '0123456789'

        s = number.replace(',', '.')

        # The number entered with letters or other symbols is an error

        if any(x not in alf for x in s):
            return False

        # Checking a fractional number

        s = s.split('/')

        # A number with several "/" characters or a single "/" character is entered - an error

        if len(s) > 2 or len(s) == 0:
            return False

        # The denominator is zero - an error

        elif len(s) == 2 and s[-1] == '0':
            return False

        for i in range(len(s)):

            if all(x not in integer for x in s[i]):
                return False

            # Checking for zero (the correct entry is "0")

            elif s[i] == '-0':
                return False

            # An erroneous record of the type "05",
            # without breaking the record of the float data type

            elif (s[i].startswith('0') and len(s[i]) != 1 and s[i][1] != '.') \
                  or (s[i].startswith('-0') and len(s[i]) > 2 and s[i][2] != '.'):

                return False

            # There are too many "." or "-" characters - an error

            elif s[i].count('-') > 1 or s[i].count('.') > 1:
                return False

            # The length of the number (if it is a fraction,
            # then the length of the denominator and numerator) must not be zero

            elif len(s[i]) == 0:
                return False

            # The number ends with a dot - error

            elif s[i].endswith('.'):
                return False

            # The number must not contain ".-"

            elif s[i].count('.-') != 0:
                return False

            # The number contains a "-",
            # but does not start with this character - error

            elif s[i].count('-') > 0 and s[i][0] != '-':
                return False

            # Checking for zero (the correct entry is "0")

            elif s[i] == '0.0':
                return False

        return True


    @staticmethod
    def _check_correct_math_operation(a: str):

        # We check that the mathematical example is of the form "number + math. operation + number"

        math_string = a.split()
        math_operations = '+-/*'

        value_to_remove_one = '('
        value_to_remove_two = ')'

        # We collect a list of numbers and mathematical operations,
        # but do not use parentheses to simplify the verification

        new_math_string = [i for i in math_string if i != value_to_remove_one and i != value_to_remove_two]

        # The mathematical example starts with a mathematical operation - error

        if new_math_string[0] in math_operations or new_math_string[-1] in math_operations:
            return False

        # Checking each number in the mathematical example by iterating through even indexes

        elif any(not(Scanner._check_correct_num(new_math_string[i])) for i in range(0, len(new_math_string), 2)):
            return False

        # Checking each mathematical operation in a mathematical example by iterating through odd indexes

        elif any(new_math_string[i] not in math_operations for i in range(1, len(new_math_string), 2)):
            return False

        return True


    @staticmethod
    def _check_correct_placement_of_parentheses(a: str):

        math_string = a.split()
        math_operation = '+-/*'

        count_error = 0
        count_opening = 0
        count_closing = 0

        # Iterating through all the characters in the list

        for i in range(len(math_string)):

            if math_string[i] == '(':
                count_opening += 1

                # Checking for empty parentheses "( )" and protecting against IndexError
                # if the opening parenthesis is at the last index of the list

                if i != len(math_string) - 1 and math_string[i + 1] == ')':
                    count_error += 1

                # The opening parenthesis is at the end, or after it there is a mathematical operation

                if i == len(math_string) - 1 or math_string[i + 1] in math_operation:
                    count_error += 1

                # There is no mathematical operation in front of the opening parenthesis,
                # or there is no other opening parenthesis in front of it,
                # while protecting the program from IndexError (i != 0)

                if i != 0 and math_string[i - 1] not in math_operation and math_string[i - 1] != '(':
                    count_error += 1

            elif math_string[i] == ')':
                count_closing += 1

                # A closing parenthesis is placed at the beginning or before it of a mathematical operation

                if i == 0 or math_string[i - 1] in math_operation:
                    count_error += 1

                # There is no mathematical operation after the closing parenthesis,
                # and there is no closing parenthesis with IndexError protection

                if i != len(math_string) - 1 and math_string[i + 1] not in math_operation and math_string[i + 1] != ')':
                    count_error += 1

        if count_error != 0 or count_opening != count_closing:
            return False

        index_opening = [i for i in range(len(math_string)) if math_string[i] == '(']
        index_closing = [i for i in range(len(math_string)) if math_string[i] == ')']

        # Checking the correct order of parentheses in a mathematical example

        for i in index_closing:

            new_index_opening = [j for j in index_opening if i > j]

            if len(new_index_opening) == 0:
                return False

        return True


    @staticmethod
    def get_type_num(inp: str):

        number = inp.strip().replace(',', '.')

        # Block for extraction and preservation of the sign ("-")

        count_minus = number.count('-')
        result = 1
        if count_minus % 2 != 0:
            result *= -1
        else:
            result *= 1


        if Scanner._check_correct_num(number):

            number = number.replace('-', '')

            # The user entered a number without a "/", checking for an integer
            # (there is no floating point or only zeros "5.0000" are written after the dot)

            if number.count('/') == 0 and (number.count('.') == 0 or (number.endswith('.0') or all(x == '0' for x in number.split('.')[1]))):

                # If there is a dot in the number,
                # split it and output only the whole part multiplied by a minus (save block "-")

                if number.count('.') == 1:
                    return int(number.split('.')[0]) * result

                return int(number) * result

            # The user entered a decimal number, but there is no "/" in the number

            elif number.count('/') == 0 and number.count('.') == 1 and not(number.endswith('.0')):

                return float(number) * result

            # Checking a number for an infinite fraction

            elif Frc._is_fraction(number):
                reduction = Reduction._to_reduction(number)

                return Frc(reduction[0] * result, reduction[1])

            # The user entered a number with a "/", but the number is not an infinite fraction

            else:

                # A fraction is not infinite, and division results in an integer

                if str(float(number.split('/')[0]) / float(number.split('/')[1])).endswith('.0'):
                    parts = number.split('/')

                    return int(str(float(parts[0]) / float(parts[1])).split('.')[0]) * result

                # A fraction is not infinite, and division results in a decimal number

                parts = number.split('/')

                return float(parts[0]) / float(parts[1]) * result

        else:
            return 'Is not correct number, try again!'