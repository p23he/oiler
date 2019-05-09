# How many, not necessarily distinct, values of n choose r for 1 <= n <= 100, are greater than one million?

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
    
def choose(n, k):
  return factorial(n) / (factorial(k) * factorial(n - k))
  
num = 0
for i in range(23, 101):
  for j in range(1, i):
    if choose(i, j) > 1000000:
      num += i - 2 * j + 1
      break
print(num)
