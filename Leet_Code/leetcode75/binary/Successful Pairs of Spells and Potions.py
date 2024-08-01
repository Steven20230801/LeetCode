import math
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # sort用於之後binary search找 >= success/spells[i] 的第一個值
        res = []

        def search_minimum(nums, target) -> int:
            l, r = 0, len(nums) - 1
            idx = len(nums)
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
                    idx = m
            # total_success = len(nums) - 1 - (r + 1) + 1 if r < len(nums) else 0
            total_success = len(nums) - idx
            return total_success

        for spell in spells:

            mini = math.ceil(success / spell)
            res.append(search_minimum(potions, mini))

        return res


Solution().successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7)
Solution().successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16)
