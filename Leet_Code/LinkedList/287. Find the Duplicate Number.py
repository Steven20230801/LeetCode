from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = [1, 3, 4, 2, 2]
        # Step 1: Find the intersection point of the two runners.
        s = nums[0]
        f = nums[0]
        while True:
            f = nums[nums[f]]
            s = nums[s]

            if f == s:
                break
        print(s, f)
        # Step 2: Find the entrance to the cycle.
        s = nums[0]
        while s != f:
            f = nums[f]
            s = nums[s]

        return s
