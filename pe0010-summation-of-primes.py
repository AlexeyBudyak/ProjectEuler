# Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

def is_prime(n):
    if n <= 1: return False
    root = int(n ** 0.5)
    for i in range(2,root+1):
        if n % i == 0: return False
    return True

def sum_primes(n):
    s = 2

    for i in range (3,n,2):
        if is_prime(i): s+= i
    return s

print(sum_primes(2000000))
