from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        l, r = 0, 1
        for r in range(len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            else:
                continue
        return l + 1


Solution().removeDuplicates([0, 0, 1, 2, 3, 4, 4, 4])
