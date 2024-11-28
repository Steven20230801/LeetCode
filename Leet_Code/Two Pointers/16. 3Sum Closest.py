from math import inf
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)
        max_diff = 99999999999
        for i in range(n - 2):
            # 跳過重複的第一個數字
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            x = nums[i]
            l, r = i + 1, n - 1

            while l < r:
                y = nums[l]
                z = nums[r]
                total = x + y + z

                if total == target:
                    return target
                else:
                    diff = x + y + z - target
                    if abs(diff) < max_diff:
                        res = total
                        max_diff = abs(diff)

                    if diff > 0:
                        r -= 1  # 需要更小的數來減少總和
                    else:
                        l += 1

        return res


Solution().threeSumClosest([0, 0, 0], 1)
Solution().threeSumClosest([-1, 2, 1, -4], 1)
