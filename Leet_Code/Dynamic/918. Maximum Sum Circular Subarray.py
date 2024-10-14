from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 求最小的sub array x, sum(nums)- x就是最大的sub array了
        n = len(nums)
        total = sum(nums)

        # 算最大
        cur_max = nums[0]
        global_max = nums[0]
        for i in range(1, n):
            cur_max = max(nums[i], cur_max + nums[i])
            global_max = max(global_max, cur_max)
        # 算最小
        cur_min = nums[0]
        global_min = nums[0]
        for i in range(1, n):
            cur_min = min(nums[i], cur_min + nums[i])
            global_min = min(global_min, cur_min)
        circle_max = total - global_min

        return max(circle_max, global_max) if total >= 0 else global_max


Solution().maxSubarraySumCircular(([5, -3, 5]))
Solution().maxSubarraySumCircular(([-2, -3, -2]))
Solution().maxSubarraySumCircular(([1, -2, 3, -2]))
# Solution().maxSubarraySumCircular()
