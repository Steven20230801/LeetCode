from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur = m + n - 1
        l, r = m - 1, n - 1  # l代表便利nums1,
        while l >= 0 and r >= 0:
            if nums1[l] <= nums2[r]:
                nums1[cur] = nums2[r]
                r -= 1
            else:
                nums1[cur] = nums1[l]
                l -= 1
            cur -= 1
        if r >= 0:
            nums1[: cur + 1] = nums2[: r + 1]
        print(nums1)


Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
Solution().merge(nums1=[1], m=1, nums2=[], n=0)
Solution().merge(nums1=[4, 5, 6, 0, 0, 0], m=3, nums2=[1, 2, 3], n=3)
