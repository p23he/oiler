n = 600851475143
factor = 2
lastFactor = 1
while n > 1:
    if n % factor == 0:
        lastFactor = factor
        n /= factor
        while n % factor == 0:
            n /= factor
        factor += 1
print(lastFactor)
