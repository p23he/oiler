#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this sequence?

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

def is_perm_wrapper(x, y):
  n = str(x)
  m = str(y)
  for c in n:
    if not c in m:
      return False 
  return True

def is_perm(x, y):
  return is_perm_wrapper(x, y) and is_perm_wrapper(y, x)

primes = erat(9999)
for p in primes:
  if p > 1000 and is_perm(p, p + 3330) and is_perm(p, p + 6660) and (p + 3330) in primes and (p + 6660) in primes:
    print(p, p+3330, p+6660)
  
