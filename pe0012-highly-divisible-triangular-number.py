n  = x = divisors = i = 0
while divisors <= 500:
    n += i
    if n > 75000000 and n % 20 == 0:
        divisors = sum ( n % x == 0 for x in range(2,int(n/2+1))) + 2
    i+= 1
print(n)
