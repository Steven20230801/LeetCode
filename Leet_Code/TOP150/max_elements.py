from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            nums.sort()
            return nums[len(nums) // 2]


Solution().majorityElement(nums=[2, 2])
Solution().majorityElement(nums=[1])
Solution().majorityElement(nums=[2, 2, 3])
