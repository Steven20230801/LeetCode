import itertools
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        def lower_bound_greater_than(nums, target):
            # 找小於sum(array) < taget的總和
            # 找大於等於target的第一個值
            l, r = 0, len(nums) - 1

            while l <= r:

                mid = (l + r) // 2
                if sum(nums[: mid + 1]) <= target:  # 若目前總額<=target, 增加數組長度
                    l = mid + 1
                else:
                    r = mid - 1
            return r + 1

        return [lower_bound_greater_than(nums, query) for query in queries]


Solution().answerQueries(nums=[4, 5, 2, 1], queries=[3, 10, 21])


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        nums.sort()
        nums = list(itertools.accumulate(nums))

        def lower_bound_greater_than(nums, target):

            # 找小於等於target的最大值下標= 大於的-1
            l, r = 0, len(nums) - 1
            while l <= r:

                mid = (l + r) // 2
                if nums[mid] <= target:  # 若目前總額<=target, 增加數組長度
                    l = mid + 1
                else:
                    r = mid - 1
            return l  # 下標 + 1 = 長度

        return [lower_bound_greater_than(nums, query) for query in queries]


Solution().answerQueries(nums=[4, 5, 2, 1], queries=[3, 10, 21])
