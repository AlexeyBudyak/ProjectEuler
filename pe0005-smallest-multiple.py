# Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divisible20(n):
    for i in range(11,20):
        if n % i != 0: return False
    return True

def smallest_multiple():
   n = 19 * 20
   while(not divisible20(n)):
       n+= 380
   return n

print(smallest_multiple())
