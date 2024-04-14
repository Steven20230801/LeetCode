from typing import List


def lower_bound(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        # print(f"left: {left}, right: {right}, mid: {mid}")
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


nums = [1, 3, 5, 6]
target = 7
print(lower_bound(nums, target))


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            # 如果有找到則直接返回
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] < target:
            return left + 1
        else:
            return left


print(Solution().searchInsert([1, 3, 5, 6], 2))
print(Solution().searchInsert([1, 3, 5, 6], 7))
