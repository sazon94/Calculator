class Reduction():

    # Euclid's algorithm
    @staticmethod
    def _gcd(a, b):
        a = abs(a)
        b = abs(b)

        while b > 0:
            a, b = b, a % b

        return a


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

            if len(new_x0) == 1:
                new_x0.append('')
            if len(new_x1) == 1:
                new_x1.append('')

            # Converting a fraction with decimal numbers into a fraction with whole numbers

            ten = max(10 ** len(new_x0[1]), 10 ** len(new_x1[1]))
            num = int(float(number[0]) * ten)
            den = int(float(number[1]) * ten)

        # The numerator and denominator contain integers

        else:
            num = int(number[0])
            den = int(number[1])

        nod = Reduction._gcd(num, den)

        num //= nod
        den //= nod

        result.append(num)
        result.append(den)

        return result