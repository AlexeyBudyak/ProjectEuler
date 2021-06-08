'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''


def table_count(add):
    line = [1]
    for i, el in enumerate(add):
        line.append(line[i] + el)
    return line[1:]

add = list(range(2,22))
for i in range(2,21):
    add = table_count(add)
    print(i,add)

print(add[-1])
