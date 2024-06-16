# recursion template
# 1. Base case
# 2. Recursive case
# 3. Return value
#
# 1. Base case: if denominator is 0, return numerator
# 2. Recursive case: if denominator is not 0, return gcd(denominator, numerator % denominator)
# 3. Return value: gcd(denominator, numerator % denominator)


def gcd(numerator, denominator):
    if denominator == 0:
        return numerator
    return gcd(denominator, numerator % denominator)


print(gcd(4, 5))  # 1
print(gcd(4, 64))  # 2
