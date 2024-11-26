class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        l, r = 0, len(s) - 1
        s: list = list(s)

        while l < r:

            while l < r and s[l] == "0":
                l += 1

            while l < r and s[r] == "1":
                r -= 1

            if l < r:
                res += r - l
                # s[l], s[r] = s[r], s[l]
                r -= 1
                l += 1

        return res


Solution().minimumSteps("1101")
Solution().minimumSteps("11000111")
