# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def is_prime(n):
    if n <= 1: return False
    root = int(n ** 0.5)
    for i in range(3,root+1):
        if n % i == 0: return False
    return True

def factors(n):
    i = 2
    if (is_prime(n)):    return [n]
    while n % i != 0: i+=1
    else:
        return [i] + factors(int(n/i))

def largest_prime(n):
    return max(factors(n))

print(largest_prime(600851475143))
