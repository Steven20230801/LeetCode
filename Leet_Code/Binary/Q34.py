def lower_bound(nums, target):  # 尋找最左邊的target index
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(f"left: {left}, right: {right}")
    return left


nums = [5, 7, 7, 8, 8, 10]
target = 8
lower_bound(nums, target)
lower_bound(nums, target + 1)

target = 6
lower_bound(nums, target)

target = 11
lower_bound(nums, target)

taget = 9
lower_bound(nums, target)


def search_range(nums, target):
    left = lower_bound(nums, target)
    right = lower_bound(nums, target + 1) - 1
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    else:
        return [left, right]


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(search_range(nums, target=8))
print(search_range(nums, target=6))


class Solution:
    def searchRange(self, nums, target):
        left = lower_bound(nums, target)
        right = lower_bound(nums, target + 1) - 1
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        else:
            return [left, right]