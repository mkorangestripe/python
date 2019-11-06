# Recursion
# Also see recursive prime number generator examples

# Converting an iterative map function to recursive
# These return cubes [1, 8, 27]

l1 = [1,2,3]

def cube(x):
    return x*x*x

def map_iter(f,lx):
    cubes = []
    for i in lx:
        cubes.append(f(i))
    return cubes

cubes = []
def map_recur(f,lx):
    if len(lx) != 0:
        i, lx = lx[0], lx[1:]
        cubes.append(f(i))
        map_recur(f, lx)
    return cubes

# As a list comprehension
[cube(i) for i in l1]


# Converting an iterative filter function to recursive
# These return numbers not divisible by 2 or 3
# [5, 7, 11, 13, 17, 19, 23]

l1 = range(2, 25)

def check_remainder(x):
    return x % 2 != 0 and x % 3 != 0

def filter_iter(f,lx):
    no_remainder = []
    for i in lx:
        if check_remainder(i):
            no_remainder.append(i)
    return no_remainder

no_remainders = []
def filter_recur(f,lx):
    if len(lx) != 0:
        i, lx = lx[0], lx[1:]
        if f(i):
            no_remainders.append(i)
        filter_recur(f, lx)
    return no_remainders

# As a list comprehension
[i for i in l1 if check_remainder(i)]


# Fibonacci sequence using memoization
# By definition, the first two numbers in the Fibonacci sequence are 1 and 1, or 0 and 1...
# depending on the chosen starting point of the sequence, and each subsequent number is the sum of the previous two.
# By using the memo, the order of growth drops from 2^n to n^2 ???

memo0 = {0:0, 1:1} ## 0, 1, 1, 2, 3, 5, 8, 13, 21
# memo1 = {0:1, 1:1} ## 1, 1, 2, 3, 5, 8, 13, 21
def fibonacci(n):
    if not n in memo0:
        memo0[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo0[n]


# The Golden Ratio
# Line segment of segments 'a' and 'b' where a+b is to 'a' as 'a' is to 'b'.
# The ration is about 1.618.  The higher the numbers in the Fibonacci sqequence, the closer their ratio to the Golden ratio.
# The Greek letter φ (phi) is used to symbolize the golden ratio.
# If a Fibonacci number is divided by its immediate predecessor in the sequence, the quotient approximates φ.
# These approximations are alternately lower and higher than φ, and converge on φ as the Fibonacci numbers increase.
# The golden spiral is a logarithmic spiral whose growth factor is φ, the golden ratio.