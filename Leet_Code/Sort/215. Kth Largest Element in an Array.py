import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, low, high, k):
            if low < high:
                pi = partition(nums, low, high)
                if pi == k:
                    return nums[pi]
                elif pi < k:
                    return quickSelect(nums, pi + 1, high, k)
                else:
                    return quickSelect(nums, low, pi - 1, k)
            return nums[low]

        def partition(nums, low, high):
            # random pivot
            pivot = random.randint(low, high)
            nums[pivot], nums[high] = nums[high], nums[pivot]
            i = low
            for j in range(low, high):
                if nums[j] < nums[high]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[high] = nums[high], nums[i]
            return i

        return quickSelect(nums, 0, len(nums) - 1, len(nums) - k)


Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
