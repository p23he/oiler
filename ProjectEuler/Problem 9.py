# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

for i in range(1, 1000):
    for j in range(1, 1000):
        sum = i ** 2 + j ** 2
        if sum ** 0.5 == math.floor(sum ** 0.5) and i + j + sum ** 0.5 == 1000:
            print(i * j * sum ** 0.5)
