from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        l, r = 0, 1
        temp = 1
        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
                temp = 1
            else:
                if temp >= 2:
                    continue
                else:
                    temp += 1
                    l += 1
                    nums[l] = nums[r]

        return l + 1


Solution().removeDuplicates([1, 2])
Solution().removeDuplicates([1, 1, 1, 2, 2, 3])
