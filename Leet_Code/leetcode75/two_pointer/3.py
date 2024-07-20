from collections import Counter


s = "pwwkew"


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        l = 0

        counter = set()
        for r in range(len(s)):

            if s[r] in counter:
                # 從左邊開始找重複的數字
                while s[l] != s[r]:
                    counter.remove(s[l])
                    l += 1
                # 找到相同的數字後(l:w r:w)
                l += 1  # 不用remove 因為目前r = w

            # 更新數字長度
            res = max(res, r - l + 1)
            # 增加出現過數字
            counter.add(s[r])

        return res


Solution().lengthOfLongestSubstring(s)
Solution().lengthOfLongestSubstring("bbbbaasadsdasddfferqwerttyuqwertyui")
