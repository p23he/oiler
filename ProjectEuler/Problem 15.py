# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are
# exactly 6 routes to the bottom right corner.
# How many much routes are there through a 20x20 grid?



import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

# Explanation: for the 2x2 case, you must take a total of 4 moves to get from one corner to the other.
# Each route can be expressed in terms of letters, for example DRRD. There must be 2 D's and 2 R's, so there are
# 4 choose 2 = 6 ways to traverse through the grid.
# For the mxn case, the number of ways is (m + n) choose n
print(choose(40, 20))
