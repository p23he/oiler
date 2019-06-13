#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

curr = 1
n = 1
temp = 0
i = 2
while len(str(n)) < 1000:
  temp = n
  n += curr
  curr = temp
  i += 1
print(n)
