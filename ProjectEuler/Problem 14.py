# Which starting number, under one million, produces the longest chain? (Collatz conjecture)

maxsofar = 0
num = 0
for i in range(1, 1000000):
  temp = i
  tempCount = 1
  while temp != 1.0:
    if temp % 2 == 0:
      temp /= 2
    else:
      temp = 3 * temp + 1
    tempCount += 1
  if tempCount > maxsofar:
    maxsofar = tempCount
    num = i
print(num)
print(maxsofar)
