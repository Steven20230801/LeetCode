# Sum of Two Integers
# leetcode.com/problems/sum-of-two-integers/
#
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.


# create answer function
def getSum(a, b):
    """
    Args:
        a (int): integer
        b (int): integer
    Returns:
        int: sum of two integers
    """
    # create a mask
    mask = 0xFFFFFFFF
    # create a carry
    carry = 0
    # loop until carry is 0
    while b & mask:
        # calculate carry
        carry = (a & b) << 1
        # calculate sum
        a = a ^ b
        # update b
        b = carry
    # return a
    return a & mask if b > mask else a


print(getSum(1, 2))
