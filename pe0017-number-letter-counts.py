'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''
def letters_in_num(num):
    num_ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
              "ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen","seventeen", "eighteen", "nineteen", "twenty"]
    num_tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if num == 1000:
        return len('one thousand') - 1
    if  num < 20:
        return len(num_ones[num])
    if num <100:
        return len(num_tens[num//10 - 2]) + len(num_ones[num % 10])
    if num % 100 == 0:
        return len(num_ones[num // 100]) + len('hundred')
    else:
        return len(num_ones[num // 100]) + len('hundred and') - 1 + letters_in_num(num % 100)

def sum_length_nums(n):
    total = 0
    for i in range(1,n + 1):
        total+= letters_in_num(i)
        print(i, total)
    return total

print(sum_length_nums(1000))
