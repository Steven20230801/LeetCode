nums = [-1, 0, 3, 5, 9, 12]

target = 12

left = 0
right = len(nums) - 1


def lower_bound(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        print(left, right)
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


lower_bound(nums, target)


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
