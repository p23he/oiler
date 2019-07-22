#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

#9 = 7 + 2×1^2
#15 = 7 + 2×2^2
#21 = 3 + 2×3^2
#25 = 7 + 2×3^2
#27 = 19 + 2×2^2
#33 = 31 + 2×1^2

#It turns out that the conjecture was false.

#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

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
