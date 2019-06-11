#What is the value of the first triangle number to have over five hundred divisors?
def numDiv(n):
    num = 0
    sqrt = int(n**0.5)
    for i in range(1, sqrt + 1):
        if n % i == 0:
            num += 2
    return num

i = 1
t = 0
while True:
    t = int((i * (i + 1)) / 2)
    if numDiv(t) > 500:
        print(t)
        break
    i += 1
