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

            if len(new_x0) > 1 and len(new_x1) == 1:
                ten = 10 ** len(new_x0[1])
                num = int(float(x[0]) * ten)
                den = int(x[1]) * ten

            elif len(new_x1) > 1 and len(new_x0) == 1:
                ten = 10 ** len(new_x1[1])
                den = int(float(x[1]) * ten)
                num = int(x[0]) * ten

            elif len(new_x1) > 1 and len(new_x0) > 1:
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