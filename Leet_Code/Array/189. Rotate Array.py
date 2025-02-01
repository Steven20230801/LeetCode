from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums2 = [0] * len(nums)

        for i, v in enumerate(nums):
            nums2[(i + k) % n] = v

        print(nums2)


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        if k != n:
            nums[: n - k], nums[n - k :] = nums[k:], nums[:k]

        print(nums)


Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
Solution().rotate([1, 2, 3, 4, 5, 6, 7], 7)
Solution().rotate(nums=[-1, -100, 3, 99], k=2)
