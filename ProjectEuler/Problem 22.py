f = open("C:\\Users\\poote\\Desktop\\p22.txt", 'r')
names = sorted(f.read().split(','))
sum = 0
i = 1
for n in names:
    for s in n:
        if s != '"':
            sum += (ord(s) - 64) * i
    i += 1
print(sum)
