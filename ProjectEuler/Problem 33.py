    import math

    # The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
    #
    # We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
    #
    # There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
    #
    # If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

    def share_del(n, d):
        sn = str(n)
        sd = str(d)
        newn = sn
        newd = sd
        result = [0, False]
        for i in range(0, len(sn)):
            for j in range(0, len(sd)):
                if sn[i] == sd[j] and sn[i] != 0:
                    newn = sn[0:i] + sn[i+1:len(sn)]
                    newd = sd[0:j] + sd[j+1:len(sd)]
                    result[1] = True
                    #print(sn, sd)
        if newn != '' and int(newd) != 0:
            result[0] = int(newn) / int(newd)
        else:
            result[0] = n / d
            result[1] = False
        return result

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    count = 0

    for d in range(2, 100):
        for n in range(1, d):
            result = n / d
            #print(n, d)
            maybe = share_del(n, d)
            if maybe[1] and maybe[0] == result:
                print(n, d, result, maybe[0])
                count += 1
    print(count)
    print(65 * 64 * 95 * 98 / gcd(16 * 26 * 19 * 49, 65 * 64 * 95 * 98))
