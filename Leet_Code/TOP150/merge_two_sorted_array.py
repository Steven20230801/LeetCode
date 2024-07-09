# leetcode 88 .
# Merge Sorted Array


from typing import List


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
        return nums1


Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # two pointers
        while m > 0 and n > 0:  # m, n > 0
            if (
                nums1[m - 1] > nums2[n - 1]
            ):  # compare the last element of nums1 and nums2
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:  # if n > 0, nums2 has remaining elements
            nums1[:n] = nums2[:n]
        return nums1


Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                nums[slow + 1] = nums[fast]
                slow += 1
            fast += 1
        return slow + 1


Solution().removeDuplicates([1, 1, 2])


def b_l(success_div_x, potions):
    l, r = 0, len(potions) - 1
    while l <= r:
        mid = (l + r) // 2

        if potions[mid] == success_div_x:
            return mid
        elif potions[mid] > success_div_x:
            l = mid + 1
        else:
            r = mid - 1
    return r


print(b_l(2.5, [1, 2, 3, 4, 5]))
