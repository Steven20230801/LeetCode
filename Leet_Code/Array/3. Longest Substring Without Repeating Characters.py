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



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0  # 左指針初始化
        char_index = {}  # 哈希表，用於記錄字符及其最新出現的位置
        max_length = 0  # 最長不重複子串的長度

        # 遍歷字符串，右指針從左到右移動
        for right, char in enumerate(s):
            # 如果字符已存在且其上一次出現的位置在當前窗口內
            if char in char_index and char_index[char] >= left:
                # 更新左指針到重複字符的下一個位置
                left = char_index[char] + 1

            # 更新字符的最新出現位置
            char_index[char] = right

            # 計算當前窗口的長度，並更新最長子串的長度
            max_length = max(max_length, right - left + 1)

        return max_length
    
Solution().lengthOfLongestSubstring("aaaaa")
Solution().lengthOfLongestSubstring("bacbb")
Solution().lengthOfLongestSubstring("")
