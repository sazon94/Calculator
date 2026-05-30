class Reduction():


    @staticmethod
    def _is_prime(x: int):
        return abs(x) > 1 and all(abs(x) % d != 0 for d in range(2, int(abs(x) ** 0.5) + 1))


    @staticmethod
    def _div(x: int):
        a = set()
        x = abs(x)
        for d in range(1, int(x ** 0.5) + 1):
            if x % d == 0:
                a.add(d)
                a.add(x // d)

        return sorted(a)


    @staticmethod
    def _to_reduction(x: str):
        x = x.split('/')
        num = 0
        den = 0

        if x[0].count('.') != 0 or x[1].count('.') != 0:
            new_x0 = x[0].split('.')
            new_x1 = x[1].split('.')

            ten = max(10 ** len(new_x0[1]), 10 ** len(new_x1[1]))
            num = int(float(x[0]) * ten)
            den = int(float(x[1]) * ten)

        else:
            num = int(x[0])
            den = int(x[1])

        a = []

        dividers_num = Reduction._div(num)
        dividers_den = Reduction._div(den)

        common_divisors = [x for x in dividers_num if x in dividers_den]

        if len(common_divisors):
            num //= common_divisors[-1]
            den //= common_divisors[-1]

        else:
            pass

        a.append(num)
        a.append(den)

        return a


class Frc():


    def __init__(self, num: int, den: int):
        if den < 0:
            num = -num
            den = -den
        self.num = num
        self.den = den


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

            if 'e' in number:
                a = number.split('e')
                num = int(a[0].replace('.', ''))
                den = 10 ** (int(a[1].replace('-', '')) + len(a[0].replace('.', '')) - 1)

            else:
                ten = 10 ** len(str(number).split('.')[1])
                num = int(float(number) * ten)
                den = ten

        return Frc(num, den)


    @staticmethod
    def _get_whole_part(x: int, y: int):
        whole_part = 0

        check_minus = 1
        if x < 0:
            check_minus = -1

        num = abs(x)
        den = y

        if num >= den:
            whole_part = num // den
            num %= den

        return whole_part * check_minus, num * check_minus, den


    def __str__(self):
        if Frc._is_fraction(f'{self.num}/{self.den}'):

            number = Frc._get_whole_part(self.num, self.den)

            if number[0] == 0:
                return f'{number[-2]}/{number[-1]}'

            else:

                if number[-2] != 0:

                    if number[-2] > 0:
                        return f'{number[0]} + {number[-2]}/{number[-1]}'

                    else:
                        return f'-({abs(number[0])} + {abs(number[-2])}/{number[-1]})'

                else:
                    return f'{number[0]}'

        else:

            if 'e' in str(self.num / self.den):

                number = str(self.num / self.den).split('e-')
                num = int(number[0].replace('.', ''))
                den = 1 * (int(number[1]) - 1)

                return '0.' + '0' * den + str(num)

            return f'{int(self.num / self.den)}' if str(self.num / self.den).endswith('.0') else f'{self.num / self.den}'


    @staticmethod
    def _is_fraction(x: str):
        a = Reduction._to_reduction(x)

        dividers_denominator = [x for x in Reduction._div(int(a[-1])) if Reduction._is_prime(x)]

        if len(dividers_denominator) == 0:
            return False

        elif int(a[-2]) % int(a[-1]) == 0:
            return False

        elif any(i not in (2, 5) for i in dividers_denominator):
            return True

        else:
            return False


    def __add__(self, other):
        if type(other) == int or type(other) == float:

            new_other = Frc.to_frc(other)

            new_num = self.num * new_other.den + new_other.num * self.den
            new_den = self.den * new_other.den

        else:
            new_num = self.num * other.den + other.num * self.den
            new_den = self.den * other.den

        reduction = Reduction._to_reduction(f'{new_num}/{new_den}')

        return Frc(reduction[0], reduction[1])


    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self, other):
        if type(other) == int or type(other) == float:

            new_other = Frc.to_frc(other)

            new_num = self.num * new_other.den - new_other.num * self.den
            new_den = self.den * new_other.den

        else:
            new_num = self.num * other.den - other.num * self.den
            new_den = self.den * other.den

        reduction = Reduction._to_reduction(f'{new_num}/{new_den}')

        return Frc(reduction[0], reduction[1])


    def __rsub__(self, other):
        if type(other) == int or type(other) == float:

            new_other = Frc.to_frc(other)

            new_num = new_other.num * self.den - self.num * new_other.den
            new_den = self.den * new_other.den

        else:
            new_num = other.num * self.den - self.num * other.den
            new_den = self.den * other.den

        reduction = Reduction._to_reduction(f'{new_num}/{new_den}')

        return Frc(reduction[0], reduction[1])


    def __mul__(self, other):
        if type(other) == int or type(other) == float:

            new_other = Frc.to_frc(other)

            new_num = self.num * new_other.num
            new_den = self.den * new_other.den

        else:
            new_num = self.num * other.num
            new_den = self.den * other.den

        reduction = Reduction._to_reduction(f'{new_num}/{new_den}')

        return Frc(reduction[0], reduction[1])


    def __rmul__(self, other):
        return self.__mul__(other)


    def __truediv__(self, other):
        if type(other) == int or type(other) == float:

            new_other = Frc.to_frc(other)

            new_num = self.num * new_other.den
            new_den = self.den * new_other.num

        else:
            new_num = self.num * other.den
            new_den = self.den * other.num

        reduction = Reduction._to_reduction(f'{new_num}/{new_den}')

        return Frc(reduction[0], reduction[1])


    def __rtruediv__(self, other):
        if type(other) == int or type(other) == float:

            new_other = Frc.to_frc(other)

            new_num = self.den * new_other.num
            new_den = self.num * new_other.den

        else:
            new_num = self.den * other.num
            new_den = self.num * other.den

        reduction = Reduction._to_reduction(f'{new_num}/{new_den}')

        return Frc(reduction[0], reduction[1])