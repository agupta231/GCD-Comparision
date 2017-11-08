# Ankur Gupta
# agupta4@wpi.edu
# CS2223 Project 1

import math
import time


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

    def determine_gcd(m_primes, n_primes):
        primes_tally = dict()

        for m in m_primes:
            if m in primes_tally:
                primes_tally[m] = [primes_tally[m][0] + 1, primes_tally[m][1]]
            else:
                count = 0

                for n in n_primes:
                    if n == m:
                        count += 1

                primes_tally[m] = [1, count]

        gcd = 1

        for prime in primes_tally.keys():
            gcd *= prime ** min(primes_tally[prime])

        return gcd

    m_primes = prime_factors(m)
    n_primes = prime_factors(n)

    return determine_gcd(m_primes, n_primes)


def effGCD(s1, s2):
    start_time_euclid = time.clock()
    gcd_euclid = euclid(s1, s2)
    end_time_euclid = time.clock()

    start_time_cica = time.clock()
    gcd_cica = cica(s1, s2)
    end_time_cica = time.clock()

    start_time_ms = time.clock()
    gcd_ms = middle_school(s1, s2)
    end_time_ms = time.clock()

    print("Euclid        -- GCD Computed: " + str(gcd_euclid) + " CPU time (seconds): " + str(end_time_euclid - start_time_euclid))
    print("CICA          -- GCD Computed: " + str(gcd_cica) + " CPU time (seconds): " + str(end_time_cica - start_time_cica))
    print("Middle School -- GCD Computed: " + str(gcd_ms) + " CPU time (seconds): " + str(end_time_ms - start_time_ms))


def effGCDAverage(s1, s2, times):
    gcd_euclid = 0
    gcd_cica = 0
    gcd_ms = 0

    start_time_euclid = time.clock()
    for i in times:
        gcd_euclid = euclid(s1, s2)
    end_time_euclid = time.clock()

    start_time_cica = time.clock()
    for i in times:
        gcd_cica = cica(s1, s2)
    end_time_cica = time.clock()

    start_time_ms = time.clock()
    for i in times:
        gcd_ms = middle_school(s1, s2)
    end_time_ms = time.clock()

    print("Euclid        -- GCD Computed: " + str(gcd_euclid) + " CPU time (seconds): " + str((end_time_euclid - start_time_euclid) / 40))
    print("CICA          -- GCD Computed: " + str(gcd_cica) + " CPU time (seconds): " + str((end_time_cica - start_time_cica) / 40))
    print("Middle School -- GCD Computed: " + str(gcd_ms) + " CPU time (seconds): " + str((end_time_ms - start_time_ms) / 40))

def UI():
    for i in range(3):
        print("\n")

        n = input("Enter the first number (n) to determine the GCD of: ")
        m = input("Enter the second number (m) to determine the GCD of: ")

        try:
            n = int(n)
            m = int(m)

            if n <= 0 or m <= 0:
                print("0 is an invalid option, try again")
                raise

            print("\n")

            effGCD(n, m)
            return

        except:
            print("Invalid input, please type in a number")

    print("Maximum of 3 attempted fulfilled. Goodbye")
    return


# UI()
