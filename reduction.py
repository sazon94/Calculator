class Reduction():

    # Checking for finding prime numbers

    @staticmethod
    def _is_prime(x: int):
        return abs(x) > 1 and all(abs(x) % d != 0 for d in range(2, int(abs(x) ** 0.5) + 1))


    # Finding all the divisors of a number

    @staticmethod
    def _div(x: int):
        dividers = set()
        x = abs(x)
        for d in range(1, int(x ** 0.5) + 1):
            if x % d == 0:
                dividers.add(d)
                dividers.add(x // d)

        return sorted(dividers)


    @staticmethod
    def _to_reduction(number: str):
        number = number.split('/')

        num = 0
        den = 0
        result = []

        # Shifting the decimal point to convert floats into integers

        if number[0].count('.') != 0 or number[1].count('.') != 0:
            new_x0 = number[0].split('.')
            new_x1 = number[1].split('.')

            # Converting a fraction with decimal numbers into a fraction with whole numbers

            ten = max(10 ** len(new_x0[1]), 10 ** len(new_x1[1]))
            num = int(float(number[0]) * ten)
            den = int(float(number[1]) * ten)

        # The numerator and denominator contain integers

        else:
            num = int(number[0])
            den = int(number[1])

        # Finding the divisors of the numerator and denominator

        dividers_num = Reduction._div(num)
        dividers_den = Reduction._div(den)

        # Finding common divisors of the numerator and denominator to reduce the fraction

        common_divisors = [x for x in dividers_num if x in dividers_den]

        # Reducing the numerator and denominator by the maximum common divisor

        if len(common_divisors):
            num //= common_divisors[-1]
            den //= common_divisors[-1]

        result.append(num)
        result.append(den)

        return result