#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# take the first element in the string, and add it to the beginning of every single permutation of the following 8 characters

def perm(string):
  l = []
  if len(string) == 2:
    return [string[0] + string[1], string[1] + string[0]]
  for i in range(0, len(string)):
    c = string[i]
    temp = perm(string[0:i] + string[i+1: len(string)])
    for j in range(0, len(temp)):
      temp[j] = c + temp[j]
    l += temp
  return l

print(perm("0123456789")[10**6 - 1])
