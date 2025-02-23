from typing import Counter, List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        ans = 0
        for v, f in counter.items():
            if f > res:
                res = f
                ans = v
        return ans


Solution().majorityElement([3, 2, 3])
