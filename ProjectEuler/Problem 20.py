# What is the sum of the digits of 100!?

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

n = str(factorial(100))
add = 0
for i in n:
    add += int(i)
print(add)
