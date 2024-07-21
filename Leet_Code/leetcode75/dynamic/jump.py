from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxn = 0  # 能跳到最遠的位子

        for i, jump in enumerate(nums):

            # 如果最大位子到的了I的話
            if maxn >= i and i + jump > maxn:
                # 更新
                maxn = i + jump
            if i > maxn:
                return False
            if maxn >= len(nums) - 1:
                return True


Solution().canJump(nums=[2, 3, 1, 1, 4])

Solution().canJump(nums=[2, 3, 0, 0, 4])

Solution().canJump(nums=[2, 0, 0])


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1  # last index

        for i in reversed(range(len(nums))):
            if i + nums[i] >= target:
                target = i
        return target == 0


Solution().canJump(nums=[2, 3, 0, 0, 4])
