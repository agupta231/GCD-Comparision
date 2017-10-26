import math

def euclid(m, n):
    while n != 0:
        r = m % n
        m = n
        n = r

    return m


def cica(m, n):
    t = min(m, n)

    while t > 0:
        if m % t == 0 and n % t == 0:
            return t
        else:
            t -= 1

    return 1


def middle_school(m, n):
    def prime_factors(num):
        start_point = math.floor(math.sqrt(num))

        while True:
            if num % start_point == 0:
                return prime_factors(start_point) + prime_factors(num / start_point)

    pass
