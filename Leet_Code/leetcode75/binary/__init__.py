def lower_bound_2(nums, target):
    # 找比0小的第一個i -> 找大於等於0的第一個i - 1
    l, r = 0, len(nums) - 1
    while l <= r:

        mid = (l + r) // 2
        if nums[mid] < target:  # 跟目標符號相反
            l = mid + 1
        else:
            r = mid - 1
    return l - 1


if __name__ == "__main__":
    nums = [-3, -2, -1, 0, 0, 1, 2]

    y = lower_bound_2(nums, 0)
