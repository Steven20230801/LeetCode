from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, low, high):
        if low < high:
            pi = self.partition(nums, low, high)
            self.quickSort(nums, low, pi - 1)
            self.quickSort(nums, pi + 1, high)

    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low
        for j in range(low, high):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i


Solution().sortArray([1, 1, 0, 2])
Solution().sortArray([5, 5, 2, 1])


class Solution:
    def sortArray(self, arr: list[int], l: int, r: int) -> list[int]:
        if r - l + 1 <= 1:
            return arr

        pivot = arr[r]
        left = l  # pointer for left side

        # Partition: elements smaller than pivot on left side
        for i in range(l, r):
            if arr[i] < pivot:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1

        # Move pivot in-between left & right sides
        arr[r] = arr[left]
        arr[left] = pivot

        # Quick sort left side
        self.sortArray(arr, l, left - 1)

        # Quick sort right side
        self.sortArray(arr, left + 1, r)

        return arr


Solution().sortArray([1, 1, 0, 2], 0, 3)


class Solution:
    def quickSort(self, nums, low, high):
        if low < high:
            pi = self.partition(nums, low, high)  # 找出pivot
            self.quickSort(nums, low, pi - 1)  # 左邊sort
            self.quickSort(nums, pi + 1, high)  # 右邊sort
        return nums

    def partition(self, nums, low, high):

        i = low
        for j in range(low, high):

            # 比較nums[low], nums[j]的關係
            if nums[j] < nums[high]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        # 轉換pivot
        nums[i], nums[high] = nums[high], nums[i]
        return i


Solution().quickSort([1, 1, 0, 2], 0, 3)
Solution().quickSort([5, 5, 2, 1], 0, 3)
