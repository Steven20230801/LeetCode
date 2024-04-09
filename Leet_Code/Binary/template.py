def lower_bound(nums, target):  # 尋找最左邊的target index
    left = 0
    right = len(nums) - 1  # -1代表閉區間

    while left <= right:  # 若區間還有元素(區間不為空)
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1  # [mid+1, right]
        else:
            right = mid - 1  # [left, mid-1]

    print(f"left: {left}, right: {right}")
    return left


arr = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
target = 7
print(lower_bound(arr, target))
