class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        n = len(s)

        # base case
        if n < 2:
            return ""

        for i, v in enumerate(s):
            # 驗證目前v的大小寫轉換是否包含在s裡面
            if v.swapcase() not in s:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1 :])

                return left if len(left) >= len(right) else right

        return s


# 2024.9.22
class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        if len(s) < 2:
            return ""

        for i, v in enumerate(s):
            if v.swapcase() not in s:
                left = self.longestNiceSubstring(s=s[:i])
                right = self.longestNiceSubstring(s=s[i + 1 :])

                return left if len(left) >= len(right) else right

        return s


Solution().longestNiceSubstring(s="bAa")
