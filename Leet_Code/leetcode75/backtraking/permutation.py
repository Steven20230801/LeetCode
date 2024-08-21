import queue
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i, non_search_nums):
            if i == n:
                ans.append(path.copy())
                return
            for x, v in enumerate(non_search_nums):

                path.append(v)
                non_search_nums.remove(v)
                dfs(i, non_search_nums)
                non_search_nums.insert(x, v)
                path.pop()

        dfs(0, nums)
        return ans


dqueue
from collections import deque


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i, non_search_nums: set):
            if i == n:
                ans.append(path.copy())
                return
            for x in non_search_nums:

                path.append(x)
                dfs(i + 1, non_search_nums - {x})
                path.pop()

        dfs(0, set(nums))
        return ans


Solution().permute([1, 2, 3])
