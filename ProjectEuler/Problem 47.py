#The first two consecutive numbers to have two distinct prime factors are:

#14 = 2 × 7
#15 = 3 × 5

#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.

#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?


import math

def erat(n):
  primes = []
  for i in range(2, n + 1):
    primes.append(i)
  i = 2
  while i < int(math.sqrt(n)):
    if i in primes:
      for j in range(i * 2, n + 1, i):
        if j in primes:
          primes.remove(j)
    i += 1
  return primes

primes = erat(1000)

def num_prime_factors(n):
    num = 0
    for i in range(0, len(primes)):
        if n % primes[i] == 0:
            n /= primes[i]
            i -= 1
            num += 1
    return num

i = 10
while num_prime_factors(i) != 4 or num_prime_factors(i + 1) != 4 or num_prime_factors(i + 2) != 4 or num_prime_factors(i + 3) != 4:
    i += 1
print(i)
