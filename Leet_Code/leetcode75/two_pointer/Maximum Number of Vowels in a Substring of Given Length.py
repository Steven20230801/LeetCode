class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        res = 0

        for r in range(len(s)):

            # + R
            ans = ans + 1 if s[r] in "aeiou" else ans
            # - L
            while r - l + 1 > k:
                ans = ans - 1 if s[l] in "aeiou" else ans
                l += 1
            # Update
            res = max(res, ans)

        return res


Solution().maxVowels(s="abciiidef", k=3)
Solution().maxVowels(s="aeiou", k=2)
Solution().maxVowels(s="leetcode", k=3)
