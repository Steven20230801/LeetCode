# sub string
from typing import List


nums = [2, 3, 1, 2, 4, 3]
target = 7


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        ans = len(nums) + 1  # 紀錄最小長度
        s = 0  # 紀錄目前答案總和
        for right_index, right_element in enumerate(nums):

            s += right_element  # 嘗試塞右邊近來
            # 盡可能排除左邊多個元素
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                ans = min(ans, right_index - left + 1)

        return ans if ans <= len(nums) else 0


nums = [1, 1, 1, 1, 1, 1, 1, 1]

target = 11


Solution().minSubArrayLen(target, nums)


len(set([1]))

tse = set()
tse.add(1)
2 in tse


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        l, r, ans = 0, 0, 0

        windows = set()
        while r < len(s):  # 從右邊開始便利
            if s[r] not in windows:  # 若目前元素不再表單上
                windows.update(s[r])  # 增加表單
                ans = max(ans, len(windows))  # 比較目前大小
                r += 1
            else:
                while s[r] in windows:
                    windows.remove(s[l])
                    l += 1
                # windows = windows[1:]
        return ans


Solution().lengthOfLongestSubstring(s="pwwkew")
Solution().lengthOfLongestSubstring(s="pwer")
Solution().lengthOfLongestSubstring(s="p")
Solution().lengthOfLongestSubstring(s="dvdf")
# [p]
# [pw]
# [pww]
# [ww]
# [w]
# [wk]
# [wke]
# [wkew]
# [kew]

nums = [1, 12, -5, -6, 50, 3]
k = 4
l, r = 0, k
nums[l:r]


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k
        now = max_sum = sum(nums[l:r])

        for s in range(k, len(nums)):
            now = now + nums[s] - nums[l]
            max_sum = max(max_sum, now)
            l += 1
            r += 1
        return max_sum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
Solution().findMaxAverage(nums, k)

nums = [0, 4, 1]
k = 1
Solution().findMaxAverage(nums, k)

nums = [0, 4, 0, 3, 2]
k = 1
Solution().findMaxAverage(nums, k)

nums = [4, 2, 1, 3, 3]
k = 2
Solution().findMaxAverage(nums, k)
