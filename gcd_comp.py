# Ankur Gupta
# agupta4@wpi.edu
# CS2223 Project 1

import time


# Function to determine GCD using Euclid's Method
def euclid(m, n):
    while n != 0:
        r = m % n
        m = n
        n = r

    return m


# Function to determine GCD using Consecutive Integer Checking Algorithm
def cica(m, n):
    t = min(m, n)

    while t > 0:
        if m % t == 0 and n % t == 0:
            return t
        else:
            t -= 1

    return 1


# Function to determine the GCD using the middle school method
def middle_school(m, n):

    # Helper function to determine the prime factors of a certain number
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

    m_primes = prime_factors(m)
    n_primes = prime_factors(n)

    gcd = 1

    if len (m_primes) < len(n_primes):
        smaller = m_primes
        bigger = n_primes
    else:
        smaller = m_primes
        bigger = n_primes

    for i in range(len(smaller)):
        for j in range(len(bigger)):
            if smaller[i] == bigger[j]:
                gcd *= smaller[i]
                bigger[j] = 0
                break

    return gcd


# Function to time all of the different GCD functions
# Given n and m, will print the GCD computed and the time taken by the various functions
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


# Debugger program to run the different GCD functions a set number of times and then to take the average of the
# runtime for each function.

# It is recommended that you input at least 40 for the number of times, as this will give a fairly decent normal curve
# a relatively good representation for the run time.
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

    # print(str((end_time_euclid - start_time_euclid)/times) + "," + str((end_time_cica - start_time_cica)/times) + "," + str((end_time_ms - start_time_ms)/times))


    print("N: " + str(s1) + " M: " + str(s2))
    print("Euclid        -- GCD Computed: " + str(gcd_euclid) + " CPU time (seconds): " + str((end_time_euclid - start_time_euclid) / times))
    print("CICA          -- GCD Computed: " + str(gcd_cica) + " CPU time (seconds): " + str((end_time_cica - start_time_cica) / times))
    print("Middle School -- GCD Computed: " + str(gcd_ms) + " CPU time (seconds): " + str((end_time_ms - start_time_ms) / times))
    print("\n")


# UI function to interact with the different GCD functions. Input is an integer > 0 and will print out the output
# from the effGCD() function.
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
effGCDAverage(89, 144, 40)
effGCDAverage(2048, 1024, 40)
effGCDAverage(12341, 12340, 40)
effGCDAverage(12341, 6170, 40)
effGCDAverage(50001, 12501, 40)
effGCDAverage(50001, 25001, 40)
effGCDAverage(94421, 96451, 40)
effGCDAverage(29, 190843, 40)
