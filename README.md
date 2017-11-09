# Project 1 - Finding the GCD

## Ankur Gupta
## CS2223

This program is fairly simple to run. There are 6 functions for the entire program:

* euclid(m, n)
* cica(m, n)
* middle_school(m, n)
* effGCD(m, n)
* effGCDAverage(m, n, times)
* UI()

By default the UI() function will automatically run, prompting you to input an m and an n
to run against all of the algorithms. The UI function will then pass the m and n into the
effGCD() function, which will time and run all of the GCD algorithms, and output the time
taken for each one.

If you want to run a function by itself, it is fairly self explanatory: just call the
function and the two numbers that you want to find the GCD of.

There is also a convenience function effGCDAverage(m, n, times). For this function, you
input 2 numbers to get the GCD of, and the number of times that you want to run the functions.
The function will then return the average time that it took to run each function on a set
of numbers.
