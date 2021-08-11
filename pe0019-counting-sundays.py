'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''


def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
date = [7, 0, 1900]
num = 0
while date[2] < 2001:
    if date[2] > 1900 and date[0] == 1:
        print(date)
        num+= 1
    date[0]+= 7
    if date[0] > months[date[1]]:
        date[0]-= months[date[1]]
        date[1]+= 1
    if date[1] == 12:
        date[1] = 0
        date[2] += 1
        months[1] = 28 + isLeapYear(date[2])

print(num)

