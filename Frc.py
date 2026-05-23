from Reduction import Reduction

class Frc():


    def __init__(self, num: int, den: int):
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
            if 'e' not in str(number):
                ten = 10 ** len(str(number).split('.')[1])
                num = round(number * ten)
                den = 1 * ten

            else:
                ten = 10 ** int(str(number)[-2:])
                num = round(number * ten)
                den = 1 * ten

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
        if Reduction._is_fraction(f'{self.num}/{self.den}'):

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
            return f'{int(self.num / self.den)}' if str(self.num / self.den).endswith('.0') else f'{self.num / self.den}'


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
