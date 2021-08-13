'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def sum_divisors(n):
    arr = [1]
    for i in range(2,int(n ** 0.5 +1)):
        if n % i == 0:
            arr.append(i)
            arr.append(n // i)
    return sum(arr)

total = 0
for x in range(2,10000):
    sd1 = sum_divisors(x)
    sd2 = sum_divisors(sd1)
    if sd2 == x and sd1 != sd2:
        total+= x
print('The sum of all the amicable numbers under 10000:', total)

