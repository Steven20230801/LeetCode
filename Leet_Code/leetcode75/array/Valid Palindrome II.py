class Solution:

    def valid(self, s):
        l, r = 0, len(s) - 1
        k = 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        k = 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.valid(s[l + 1 : r + 1]) or self.valid(s[l:r])
        return True


Solution().validPalindrome("abca")
Solution().validPalindrome("aba")
Solution().validPalindrome("abc")
