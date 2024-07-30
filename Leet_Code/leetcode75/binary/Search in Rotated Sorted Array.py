from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 首先找到下標是谷底的 nums[i] < nums[i-1] and nums[i] < nums[i+1]

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        def findmin(nums: List[int]) -> int:

            l, r = 0, len(nums) - 1
            res = 0  # 假設 nums[0]是最小值
            while l <= r:
                # if sorted
                if nums[l] < nums[r]:
                    res = res if nums[res] < nums[l] else l
                    return res

                m = (l + r) // 2
                res = res if nums[res] < nums[m] else m

                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m - 1

            return res

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

        min_index = findmin(nums)

        if target >= nums[min_index] and target <= nums[-1]:

            if find_target_index(nums[min_index:], target) != -1:
                return min_index + find_target_index(nums[min_index:], target)
            else:
                return -1
        else:
            return find_target_index(nums[:min_index], target)


Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)

Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3)

Solution().search(nums=[3, 1], target=3)

Solution().search(nums=[1, 3], target=1)

Solution().search(nums=[3, 4, 5, 6, 1, 2], target=2)

Solution().search(nums=[5, 1, 3], target=2)
