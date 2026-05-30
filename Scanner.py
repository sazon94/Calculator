from Frc import Frc, Reduction


class Scanner():


    @staticmethod
    def _check_correct_num(a: str):
        number = a
        alf = '0123456789-/.,'
        integer = '0123456789'

        s = number.replace(',', '.')

        if any(x not in alf for x in s):
            return False

        elif s == '':
            return False

        s = s.split('/')

        if len(s) > 2 or len(s) == 0:
            return False

        elif len(s) == 2 and s[-1] == '0':
            return False

        for i in range(len(s)):
            if all(x not in integer for x in s[i]):
                return False

            elif s[i] == '-0':
                return False

            elif (s[i].startswith('0') and len(s[i]) != 1 and s[i][1] != '.') \
                  or (s[i].startswith('-0') and len(s[i]) > 2 and s[i][2] != '.'):

                return False

            elif s[i].count('-') > 1 or s[i].count('.') > 1:
                return False

            elif len(s[i]) == 0:
                return False

            elif s[i].endswith('.'):
                return False

            elif s[i].count('.-') != 0:
                return False

            elif s[i].count('-') > 0 and s[i][0] != '-':
                return False

            elif s[i] == '0.0':
                return False

        return True


    @staticmethod
    def _check_correct_math_operation(a: str):
        math_string = a.split()
        math_operations = '+-/*'

        if math_string[0] in math_operations or math_string[-1] in math_operations:
            return False

        elif any(not(Scanner._check_correct_num(math_string[i])) for i in range(0, len(math_string), 2)):
            return False

        elif any(len(math_string[i]) != 1 for i in range(1, len(math_string), 2)):
            return False

        return True



    @staticmethod
    def get_type_num(inp: str):
        number = inp.strip().replace(',', '.')
        count_minus = number.count('-')
        result = 1

        if count_minus % 2 != 0:
            result *= -1
        else:
            result *= 1

        if Scanner._check_correct_num(number):

            number = number.replace('-', '')

            if number.count('/') == 0 and (number.count('.') == 0 or (number.endswith('.0') or all(x == '0' for x in number.split('.')[1]))):

                if number.count('.') == 1:
                    return int(number.split('.')[0]) * result

                return int(number) * result

            elif number.count('/') == 0 and number.count('.') == 1 and not(number.endswith('.0')):

                return float(number) * result

            elif Frc._is_fraction(number):
                reduction = Reduction._to_reduction(number)

                return Frc(reduction[0] * result, reduction[1])

            else:

                if str(float(number.split('/')[0]) / float(number.split('/')[1])).endswith('.0'):
                    parts = number.split('/')

                    return int(str(float(parts[0]) / float(parts[1])).split('.')[0]) * result

                parts = number.split('/')

                return float(parts[0]) / float(parts[1]) * result

        else:
            return 'Is not correct number, try again!'