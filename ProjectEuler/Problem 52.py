# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def same_com(x, mult):
  xstr = str(x)
  multstr = str(mult)
  for c in multstr:
    if not c in xstr:
      return False
    else:
      xstr = xstr.replace(c, '')
  return True

def check_mult(x):
  for i in range(2, 7):
    if not (same_com(x, i * x) and same_com(i * x, x)):
      return False
  return True

x = 1
while not check_mult(x):
  x += 1
print(x)
