# Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def triplet100():
    for a in range (1,1000):
        for b in range (a+1,(1000 - a)//2):
            c = 1000 - b - a
            if a * a + b * b == c * c:
                return a * b * c

print(triplet100())
