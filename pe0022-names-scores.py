file = open("pe0022-names.txt", 'r')
names = file.read().split(',')
file.close()
names.sort()
total = sum([sum([ord(c) - 64 for c in name[1:-1]]) * (i + 1) for i,name in enumerate(names)])
print(total)
