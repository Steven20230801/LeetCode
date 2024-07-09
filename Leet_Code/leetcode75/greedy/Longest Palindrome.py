from collections import Counter

# Palindrome: 2n k + (2n+1) n


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        counter = Counter(s)
        for st in counter:
            # 每個k盡可能拿最多的偶數個
            ans += 2 * (counter[st] // 2)
            # 若有奇數的話則多加一個進來(最多就只能加一個)
            if ans % 2 == 0 and counter[st] % 2 == 1:
                ans += 1
        return ans


Solution().longestPalindrome(s="abccccdd")
Solution().longestPalindrome(s="a")
