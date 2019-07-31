#Let B(n)=∏k=0n(nk), a product of binomial coefficients.
#For example, B(5)=(50)×(51)×(52)×(53)×(54)×(55)=1×5×10×10×5×1=2500.

#Let D(n)=∑d|B(n)d, the sum of the divisors of B(n).
#For example, the divisors of B(5) are 1, 2, 4, 5, 10, 20, 25, 50, 100, #125, 250, 500, 625, 1250 and 2500,
#so D(5) = 1 + 2 + 4 + 5 + 10 + 20 + 25 + 50 + 100 + 125 + 250 + 500 + 625 + 1250 + 2500 = 5467.

#Let S(n)=∑k=1nD(k).
#You are given S(5)=5736, S(10)=141740594713218418 and S(100) mod 1000000007=332792866.

#Find S(20000) mod 1000000007.

#https://projecteuler.net/problem=650
#https://math.stackexchange.com/questions/964267/proofs-of-identity-for-product-of-binomial-coefficients

def fact(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

def choose(n, k):
  return fact(n) / (fact(k) * fact(n - k))

def b(n):
  prod = 1
  for k in range(1, n + 1):
    prod *= k**(2 * k - n - 1)
  return int(prod)

def d(n):
  sum = 0
  bn = b(n)
  for i in range(1, bn + 1):
    if bn % i == 0:
      sum += i# % 10**9 + 7
  return sum

def s(n):
  sum = 0
  for k in range(1, n + 1):
    sum += d(k)
  return sum

print(s(10))
