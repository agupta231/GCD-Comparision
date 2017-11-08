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
        factors = []
        i = 2
        n = num

        while n > 1:
            if n % i == 0:
                factors.append(i)
                n = n / i
                i -= 1

            i += 1

        return factors

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
    for i in range(times):
        gcd_euclid = euclid(s1, s2)
    end_time_euclid = time.clock()

    start_time_cica = time.clock()
    for i in range(times):
        gcd_cica = cica(s1, s2)
    end_time_cica = time.clock()

    start_time_ms = time.clock()
    for i in range(times):
        gcd_ms = middle_school(s1, s2)
    end_time_ms = time.clock()

    print("N: " + str(s1) + " M: " + str(s2))
    print("Euclid        -- GCD Computed: " + str(gcd_euclid) + " CPU time (seconds): " + str((end_time_euclid - start_time_euclid) / times))
    print("CICA          -- GCD Computed: " + str(gcd_cica) + " CPU time (seconds): " + str((end_time_cica - start_time_cica) / times))
    print("Middle School -- GCD Computed: " + str(gcd_ms) + " CPU time (seconds): " + str((end_time_ms - start_time_ms) / times))
    print("\n")


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

effGCDAverage(31415, 14142, 40)
effGCDAverage(8, 13, 40)
effGCDAverage(8, 21, 40)
effGCDAverage(13, 21, 40)
effGCDAverage(50, 11, 40)
effGCDAverage(50, 23, 40)
effGCDAverage(50000, 12501, 40)
effGCDAverage(50000, 25001, 40)
effGCDAverage(475928, 234858, 40)
effGCDAverage(2295976, 1895576, 40)
