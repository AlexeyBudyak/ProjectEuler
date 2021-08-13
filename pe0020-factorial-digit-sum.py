'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''


def add_long_nums(s1, s2):
    if len(s2) > len(s1):
        s1, s2 = s2, s1
    s1 = list(s1)
    s2 = list(s2)
    n = 0
    s1 = s1[::-1] + ['0'] * (s1[0] != '0')
    s2 = s2[::-1] + ['0'] * (len(s1) - len(s2))
    for i in range(len(s1)):
        n = int(s1[i]) + int(s2[i]) + n
        s1[i] = str(n % 10)
        n = n // 10
    return ''.join(s1[::-1])

def mult_long_nums(s, n):
    total = '0'
    for i in range(n):
        total = add_long_nums(total, s)
    return total

factorial = '1'
for n in range(100,1,-1):
    factorial = mult_long_nums(factorial, n)

sum_factorial = sum(list(map(int, factorial)))
print('Sum of the digits in the number 100!:',sum_factorial)
