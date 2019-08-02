#The square root of 2 can be written as an infinite continued fraction.

#2–√=1+12+12+12+12+...
#The infinite continued fraction can be written, 2–√=[1;(2)], (2) #indicates that 2 repeats ad infinitum. In a similar way, 23−−√=[4;(1,3,1,8)].

#It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for 2–√.

#1+12=321+12+12=751+12+12+12=17121+12+12+12+12=4129
#Hence the sequence of the first ten convergents for 2–√ are:

#1,32,75,1712,4129,9970,239169,577408,1393985,33632378,...
#What is most surprising is that the important mathematical constant,
#e=[2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...].

#The first ten terms in the sequence of convergents for e are:

#2,3,83,114,197,8732,10639,19371,1264465,1457536,...
#The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

#Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

# for personal use ;-;
# 2 + 1/1 = 3
# 2 + 1/(1 + 1/2) = 8/3
# 2 + 1/(1 + 1/(2 + 1/1)) = 11/4
# 2 + 1/(1 + 1/(2 + 1/(1 + 1/1))) = 19/7
# 2 + 1/(1 + 1/(2 + 1/(1 + 1/(1 + 1/4)))) = 87/32
# 2 + 1/(1 + 1/(2 + 1/(1 + 1/(1 + 1/(4 + 1/1))))) = 106/39
# 2 + 1/39/28) 

total = 0
# the 2nd convergence is k = 2, the 5th convergence is k = 4, ... the 98th convergence is k = 66
k = 66

# go through each expansion
# each expansion will go through a loop itself
fraction = [1, 1]# the last fraction in the 100th convergence is 1/1
for i in range(98, -1, -1):
  n = fraction[0]
  d = fraction[1]
  if i != 0 and i % 3 == 2:
    fraction = [d, d * k + n]
    k -= 2
  elif i != 0:
    fraction = [d, d + n]
  elif i == 0:
    fraction = [n + d * 2, d]

for c in str(fraction[0]):
  total += int(c)
print(total)
