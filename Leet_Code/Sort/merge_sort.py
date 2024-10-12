def merge_sort(arr):
    """
    將輸入的陣列進行合併排序並返回排序後的陣列。
    """
    if len(arr) <= 1:
        return arr

    # 分割陣列為左右兩部分
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 合併已排序的左右兩部分
    return merge(left_half, right_half)


def merge(left, right):
    """
    合併兩個已排序的陣列並返回合併後的排序陣列。
    """
    merged = []
    left_index = right_index = 0

    # 比較左右兩邊的元素，將較小的元素加入合併陣列
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # 將剩餘的元素加入合併陣列
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# 範例使用
if __name__ == "__main__":
    unsorted_array = [38, 27, 43, 3, 9, 82, 10]
    print("未排序的陣列:", unsorted_array)
    sorted_array = merge_sort(unsorted_array)
    print("排序後的陣列:", sorted_array)

    unsorted_array = [4, 3, 2, 1]
    print("未排序的陣列:", unsorted_array)
    sorted_array = merge_sort(unsorted_array)
    print("排序後的陣列:", sorted_array)
