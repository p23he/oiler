#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

#(Please note that the palindromic number, in either base, may not include leading zeros.)

def is_palindrome(string):
    for i in range(0, int(len(string) / 2)):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True


total = 0

for i in range(1, 10**6 + 1):
    if is_palindrome(str(i)) and is_palindrome(str(bin(i))[2:]):
        print(i, bin(i))
        total += i
print(total)
