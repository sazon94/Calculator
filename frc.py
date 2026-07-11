from reduction import Reduction

class Frc():


    def __init__(self, num: int, den: int):
        if den < 0:
            num = -num
            den = -den
        self.num = num
        self.den = den


    # Converting int and float to Frc

    @staticmethod
    def to_frc(number: int|float):
        tp = type(number)
        num = 0
        den = 0

        if tp == int:
            num = number
            den = 1

        elif tp == float:
            number = str(number)

            # Float to Frc translation unit, considering exponential notation

            if 'e-' in number:
                a = number.split('e')
                num = int(a[0].replace('.', ''))
                den = 10 ** (int(a[1].replace('-', '')) + len(a[0].replace('.', '')) - 1)

            elif 'e+' in number:
                a = number.split('e')
                ten = 10 ** (int(a[1]) - (len(a[0]) - len(a[0].split('.')[0]) - a[0].count('.')))
                num = int(a[0].replace('.', '')) * ten
                den = 1

            else:
                ten = 10 ** len(str(number).split('.')[1])
                num = int(float(number) * ten)
                den = ten

        else:
            return number

        return Frc(num, den)


    @staticmethod
    def _get_whole_part(x: int, y: int):
        whole_part = 0
        num = abs(x)
        den = y

        check_minus = 1
        if x < 0:
            check_minus = -1

        if num >= den:
            whole_part = num // den
            num %= den

        return whole_part * check_minus, num * check_minus, den


    def __str__(self):

        if Frc._is_fraction(f'{self.num}/{self.den}'):

            return f'{self.num}/{self.den}'

        else:

            # Convenient output (for the user) of an exponential number representation

            if 'e-' in str(self.num / self.den):

                number = str(self.num / self.den).split('e-')

                if '-' not in number[0]:

                    num = int(number[0].replace('.', ''))
                    den = 1 * (int(number[1]) - 1)

                    return '0.' + '0' * den + str(num)

                else:
                    num = int(number[0].replace('.', '').replace('-', ''))
                    den = 1 * (int(number[1]) - 1)

                    return '-0.' + '0' * den + str(num)

            elif 'e+' in str(self.num / self.den):

                number = str(self.num / self.den).split('e+')
                base = number[0]
                exponent = int(number[1])

                if '.' in base:
                    int_part, frac_part = base.split('.')
                    zeros_needed = exponent - len(frac_part)

                    return int_part + frac_part + ('0' * zeros_needed if zeros_needed > 0 else '')

                else:
                    return base + '0' * exponent

            return f'{int(self.num / self.den)}' if str(self.num / self.den).endswith('.0') else f'{self.num / self.den}'


    # Checking if the fractions results in a repeating (periodic) decimal

    @staticmethod
    def _is_fraction(x: str):
        number = Reduction._to_reduction(x)

        dividers_denominator = [x for x in Reduction._div(int(number[-1])) if Reduction._is_prime(x)]

        if len(dividers_denominator) == 0:
            return False

        elif int(number[-2]) % int(number[-1]) == 0:
            return False

        elif any(i not in (2, 5) for i in dividers_denominator):
            return True

        else:
            return False


    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den

        reduction = Reduction._to_reduction(f'{new_num}/{new_den}')

        return Frc(reduction[0], reduction[1])


    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den

        reduction = Reduction._to_reduction(f'{new_num}/{new_den}')

        return Frc(reduction[0], reduction[1])


    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den

        reduction = Reduction._to_reduction(f'{new_num}/{new_den}')

        return Frc(reduction[0], reduction[1])


    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num

        reduction = Reduction._to_reduction(f'{new_num}/{new_den}')

        return Frc(reduction[0], reduction[1])