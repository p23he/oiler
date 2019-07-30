#Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

#n	Relatively Prime	φ(n)	        n/φ(n)
#2	1	                1             2
#3	                  1,2	2	        1.5
#4	                  1,3	2	        2
#5	                  1,2,3,4	4	    1.25
#6	                  1,5	2	        3
#7	                  1,2,3,4,5,6	6	1.1666...
#8	                  1,3,5,7	4	    2
#9	                  1,2,4,5,7,8	6	1.5
#10	                  1,3,7,9	4	    2.5
#It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

#Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

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

def φ(n): #not needed, was for inital attempt
  total = 0
  for i in range(1, n):
    if math.gcd(i, n) == 1:
      total += 1
  return total

# by wikipedia, phi(n) = n * prod(1 - 1/p) for all p|n
# so n / phi(n) is 1/prod(1 - 1/p)
# meaning we need to minimize prod(1 - 1/p)
# meaning we need lots of primes
primes = erat(500)
n = 1
i = 0
while n * primes[i] <= 10**6:
  n *= primes[i]
  i += 1
print(n)
