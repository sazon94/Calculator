from Frc import Frc
from Reduction import Reduction


class Scanner():


    @staticmethod
    def _check_correct_num(a: str):
        number = a
        alf = '0123456789-/.,'
        integer = '0123456789'

        s = number.replace(',', '.')

        if any(x not in alf for x in s):
            return 'You bad'

        elif s == '':
            return 'You bad'

        s = s.split('/')

        if len(s) > 2 or len(s) == 0:
            return 'You bad'

        elif len(s) == 2 and s[-1] == '0':
            return 'You bad'

        for i in range(len(s)):
            if all(x not in integer for x in s[i]):
                return 'You bad'

            elif s[i] == '-0':
                return 'You bad'

            elif (s[i].startswith('0') and len(s[i]) != 1 and s[i][1] != '.') \
                  or (s[i].startswith('-0') and len(s[i]) > 2 and s[i][2] != '.'):

                return 'You bad'

            elif s[i].count('-') > 1 or s[i].count('.') > 1:
                return 'You bad'

            elif len(s[i]) == 0:
                return 'You bad'

            elif s[i].endswith('.'):
                return 'You bad'

            elif s[i].count('.-') != 0:
                return 'You bad'

            elif s[i].count('-') > 0 and s[i][0] != '-':
                return 'You bad'

            elif s[i] == '0.0':
                return 'You bad'

        return 'You cool man'


    @staticmethod
    def get_type_num(inp: str):
        number = inp.strip().replace(',', '.')
        count_minus = number.count('-')
        result = 1

        if count_minus % 2 != 0:
            result *= -1
        else:
            result *= 1

        if Scanner._check_correct_num(number) == 'You cool man':

            number = number.replace('-', '')

            if number.count('/') == 0 and (number.count('.') == 0 or (number.endswith('.0') or all(x == '0' for x in number.split('.')[1]))):

                if number.count('.') == 1:
                    return int(number.split('.')[0]) * result

                return int(number) * result

            elif number.count('/') == 0 and number.count('.') == 1 and not(number.endswith('.0')):

                return float(number) * result

            elif Reduction._is_fraction(number):
                reduction = Reduction._to_reduction(number)

                if count_minus % 2 == 0:
                    return Frc(reduction[0], reduction[1])

                else:
                    return Frc(reduction[0] * result, reduction[1])

            else:

                if str(float(number.split('/')[0]) / float(number.split('/')[1])).endswith('.0'):
                    parts = number.split('/')

                    return int(str(float(parts[0]) / float(parts[1])).split('.')[0]) * result

                parts = number.split('/')

                return float(parts[0]) / float(parts[1]) * result

        else:
            return 'Is not correct number, try again!'