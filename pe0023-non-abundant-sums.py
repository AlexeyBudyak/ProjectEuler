def is_abundant(n):
    if n < 12: return False
    arr = [1]
    for i in range(2,int(n ** 0.5 +1)):
        if n % i == 0:
            arr.append(i)
            arr.append(n // i)
    arr = list(set(arr))
    return sum(arr) > n

ab = []
for x in range(12, 28124):
    if is_abundant(x):
        ab.append(x)
ab_sums = list(set([j + i for i in ab for j in ab]))
total = sum([x * (x not in ab_sums) for x in range(1,28124)])
print(total)
