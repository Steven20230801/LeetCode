from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = set()
        L = 0
        for R in range(len(nums)):

            while R - L > k:
                check.remove(nums[L])
                L += 1

            if nums[R] in check:
                return True

            check.add(nums[R])

        return False


Solution().containsNearbyDuplicate([1, 2, 1], 0)
