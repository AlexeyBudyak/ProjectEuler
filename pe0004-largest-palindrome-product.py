# Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_prime(n):
    if n <= 1: return False
    root = int(n ** 0.5)
    for i in range(3,root+1):
        if n % i == 0: return False
    return True

def palindrome():
   s = []
   for i in range(999,100,-1):
       for j in range(999,100,-1):
           c = str(i * j)
           if(c == c[::-1]): s.append(int(c))
   return s

def largest_palindrome():
    return max(palindrome())

print(largest_palindrome())
