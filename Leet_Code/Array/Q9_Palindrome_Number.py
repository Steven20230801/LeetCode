# Palidrome Number
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:
# Input: 121
# Output: true


def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    else:
        return str(x) == str(x)[::-1]


# Two Pointers
# Time: O(n)
# Space: O(1)
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    else:
        x = str(x)
        left = 0
        right = len(x) - 1
        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True


isPalindrome(121)
isPalindrome(-121)
isPalindrome(10)
