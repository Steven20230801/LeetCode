class Solution:
    def longestPalindrome(self, s: str) -> str:

        def calculate_max_palidrome(l, r):
            max_res = 0
            ans = [l, r]
            # s[l:r+1] 如果是palidrome 就持續增加到邊界 看最大能多長
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res = r - l + 1
                if res > max_res:
                    max_res = res
                    ans = [l, r]
                l -= 1
                r += 1
            return max_res, ans

        max_res = 0
        ans = [0, 0]  # 初始化答案
        for i in range(0, len(s)):

            # odd
            odd = calculate_max_palidrome(i, i)
            even = calculate_max_palidrome(i, i + 1)

            if odd[0] > max_res:
                max_res = odd[0]
                ans = odd[1]
            if even[0] > max_res:
                max_res = even[0]
                ans = even[1]

        return s[ans[0] : ans[1] + 1]


Solution().longestPalindrome("babad")
