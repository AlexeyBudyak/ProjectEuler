n  = x = divisors = i = 0
while divisors <= 500:
    n += i
    sqrt = n ** 0.5
    divisors = sum ( n % x == 0 for x in range(2,int(sqrt+1))) * 2 + 2 - (sqrt % 1 == 0)
    i+= 1
print(n, divisors)
