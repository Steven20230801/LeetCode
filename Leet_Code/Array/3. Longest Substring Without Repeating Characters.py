from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        ans = 0
        h = defaultdict(int)
        while r < len(s):

            h[s[r]] += 1

            while h[s[r]] > 1:
                h[s[l]] -= 1
                l += 1

            res = r - l + 1
            ans = max(ans, res)

            r += 1

        return ans


Solution().lengthOfLongestSubstring("aaaaa")
Solution().lengthOfLongestSubstring("bacbb")
Solution().lengthOfLongestSubstring("")
