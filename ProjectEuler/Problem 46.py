def isPrime(n):
    upp = math.floor(math.sqrt(n))
    for i in range(2, upp + 1):
        if n % i == 0:
            return False
    return True

n = 9
while True:
    if (not isPrime(n)):
        i = 1
        while True:
            if n - 2 * i * i <= 0:
                print(n)
                break
            if not isPrime(n - 2 * i * i):
                i += 1
            else:
                break
    n += 2
# it finds all such numbers, so I just took the first one
