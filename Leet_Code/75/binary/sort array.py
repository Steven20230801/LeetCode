from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 首先找到下標是谷底的 nums[i] < nums[i-1] and nums[i] < nums[i+1]

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        def findPeakElement(nums: List[int]) -> int:
            nums.append(float("-inf"))
            nums.insert(0, float("-inf"))

            l, r = 0, len(nums) - 1

            # 若mid左邊比較大, 左邊是封頂, 右邊比較大, 右邊是封頂

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid - 1

                elif nums[mid] > nums[mid - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

            return l

        x = findPeakElement(nums)
        nums = nums[1 : len(nums) - 1]

        def find_target_index(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid

                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        # 如果target >= nums[0] and tager <= nums[x-1](封頂), target要在左邊找
        # 或是根本沒轉 x = 0

        if target >= nums[0] and target <= nums[x]:

            return find_target_index(nums[: x + 1], target)

        else:
            # 右邊開始找的話要加上x長度

            ans = find_target_index(nums[x + 1 :], target)

            if ans == -1:
                return -1
            else:
                return ans + (x + 1)





class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 先去找到中間的轉折點
        # 這樣就可以分成兩個sorted array
        # 再去找target

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
            
        def findPeakElement(nums: List[int]) -> int:
            


Solution().search([3, 4, 5, 6, 1, 2], 2)

Solution().search([1, 3], 3)
Solution().search([3, 1], 1)

Solution().search([7, 8, 1, 2, 3, 4, 5, 6], 2)
