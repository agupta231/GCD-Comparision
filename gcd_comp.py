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
    pass


def prime_factors(num):
    if is_prime(num):
        return [num]

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return prime_factors(i) + prime_factors(int(num / i))


def is_prime(val):
    if val == 2:
        return True

    for i in range(2, int(math.ceil(math.sqrt(val))) + 1):
        if val % i == 0:
            return False

    return True