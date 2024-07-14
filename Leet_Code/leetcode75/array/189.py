from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = nums[-k:] + nums[:-k]
        return nums


Solution().rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)


def rotate(nums, k):
    n = len(nums)
    k = k % n  # 當 k 大於 n 時，只需旋轉 k % n 次

    count = 0  # 計數已經處理的元素數量
    start = 0  # 從頭開始

    while count < n:
        current = start  # 要調換的下標
        prev = nums[start]  # 要調換的數字
        while True:
            next_idx = (current + k) % n  # 被調換的下標
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1

            if start == current:
                break
        start += 1


# 測試範例
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print(nums)  # 輸出結果應為 [5, 6, 7, 1, 2, 3, 4]
