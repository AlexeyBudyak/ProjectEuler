# Sum square difference
#
# The sum of the squares of the first ten natural numbers is,
#
# The square of the sum of the first ten natural numbers is,
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_squares_diff(n):
    a = list(range(1,n+1))
    b = list(map(lambda c: c * c,a))
    return sum(a) ** 2 - sum(b)

print(sum_squares_diff(100))
