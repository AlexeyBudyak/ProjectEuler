'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def collatz(n):
    i = 1
    while n != 1:
        if n % 2:   n = 3 * n + 1
        else:       n /= 2
        i+= 1
    return i
longest_chain = [2, 2]

for i in range(2,1000000):
    x = collatz(i)
    if x > longest_chain[1]: longest_chain = [i, x]
print(longest_chain)
