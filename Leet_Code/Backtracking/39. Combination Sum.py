from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(candidates)

        def dfs(i):

            # base case sum(path) = target
            if sum(path) == target:
                res.append(path.copy())
                return
            # edge
            if i == n:
                return

            # 選candidates[i]的情況
            if target - sum(path) >= candidates[i]:
                path.append(candidates[i])
                dfs(i)
                path.pop()

            dfs(i + 1)

        dfs(0)
        return res


Solution().combinationSum(candidates=[2, 3, 6, 7], target=7)
