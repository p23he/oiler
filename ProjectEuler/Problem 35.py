#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

#How many circular primes are there below one million?

import math

def is_prime(n):
    upp = math.floor(math.sqrt(n))
    for i in range(2, upp + 1):
        if n % i == 0:
            return False
    return True

def is_circ(p):
  temp = str(p)[1:len(str(p))] + str(p)[0:1]
  for i in range(1, len(temp)):
    if not is_prime(int(temp)):
      return False
    temp = temp[1:len(temp)] + temp[0:1]
  return True

total = 0
for i in range(2, 1000000):
  if is_prime(i) and is_circ(i):
    total += 1
print(total)
