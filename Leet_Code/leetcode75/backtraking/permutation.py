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
                dfs(i + 1, non_search_nums - {v})
                path.pop()

        dfs(0, set(nums))

        return ans


Solution().permute([1, 2, 3])
