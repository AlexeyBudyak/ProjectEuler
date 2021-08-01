def add_long_nums(s1,s2):
    n = 0
    s1 = s1[::-1] + ['0'] * (s1[0] != '0')
    s2 = s2[::-1] + ['0'] * (len(s1) - len(s2))
    for i in range(len(s1)):
        n = int(s1[i]) + int(s2[i]) + n
        s1[i] = str(n % 10)
        n = n // 10
    return s1[::-1]

num = ['2']
for i in range(2,1001):
    num = add_long_nums(num, num)
s = sum([int(el) for el in num])
print(s)
