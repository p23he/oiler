# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
#where each “_” is a single digit.

import math

lower = int(math.sqrt(1020304050607080900))
upper = int(math.sqrt(1929394959697989990))

print(lower, upper)

for i in range(lower, upper, 10):
  s = str(i**2)
  if s[0] == '1' and s[2] == '2' and s[4] == '3' and s[6] == '4' and s[8] == '5' and s[10] == '6' and s[12] == '7' and s[14] == '8' and s[16] == '9' and s[18] == '0':
    print(i)
    break
