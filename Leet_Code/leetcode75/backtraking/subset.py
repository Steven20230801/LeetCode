from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)  # 1, 2

        def dfs(i):
            # 終止條件
            if i == n:
                res.append(path.copy())
                return

            # 選1 or 不選1
            # 1. 選1
            path.append(nums[i])
            dfs(i + 1)  # 選2環節
            path.pop()  # 因為共用list, 需要還原

            # 2. 不選1
            ...  # 不用動作
            dfs(i + 1)
            ...  # 不用還原

        dfs(i=0)
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)  # 1, 2

        def dfs(i):
            # 終止條件
            if i == n:
                res.append(path.copy())
                return

            # 選1 or 不選1
            # 1. 選1
            path.append(nums[i])
            dfs(i + 1)  # 選2環節
            path.pop()  # 因為共用list, 需要還原

            # 2. 不選1
            ...  # 不用動作
            dfs(i + 1)
            ...  # 不用還原

        dfs(i=0)
        return res


Solution().subsets(nums=[1])
