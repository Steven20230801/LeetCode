from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        i = 0
        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            i += 1

        if i == len(nums) - 1:
            return True

        if nums[i] > nums[i + 1]:

            # 確認降序
            while i < len(nums) - 1:
                if nums[i] < nums[i + 1]:
                    return False
                i += 1

        else:

            while i < len(nums) - 1:
                if nums[i] > nums[i + 1]:
                    return False
                i += 1

        return True

    def isMonotonic(self, nums: List[int]) -> bool:

        increasing, decreasing = True, True

        for i in range(len(nums) - 1):

            if not (nums[i] <= nums[i + 1]):
                increasing = False

            if not (nums[i] >= nums[i + 1]):
                decreasing = False

        return increasing or decreasing


test1 = [1, 1, 0]
test2 = [1, 2, 3, 4]
test3 = [1, 1, 1, 5]
test4 = [1, 2, 1]

Solution().isMonotonic(test1)
Solution().isMonotonic(test2)
Solution().isMonotonic(test3)
Solution().isMonotonic(test4)
