# 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

def is_prime(n):
    if n <= 1: return False
    root = int(n ** 0.5)
    for i in range(2,root+1):
        if n % i == 0: return False
    return True

def n_prime(n):
    s = 1; i = 3
    while s < n:
        if is_prime(i):
            s+=1
        i+=2
    return i-2


print(n_prime(10001))
