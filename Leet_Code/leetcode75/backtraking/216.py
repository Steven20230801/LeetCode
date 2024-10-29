from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
        path = []

        def dfs(i, remain):
            if len(path) == k:
                if remain == 0:
                    res.append(path[:])
                return
            for j in range(i, 10):
                if j > remain:
                    break
                path.append(j)
                dfs(j + 1, remain - j)
                path.pop()

        dfs(1, n)
        return res


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
        path = []

        def dfs(i, remain):
            if len(path) == k and remain == 0:
                res.append(path[:])
                return

            if remain < 0 or i > 9:
                return

            path.append(i)
            dfs(i + 1, remain - i)
            path.pop()

            dfs(i + 1, remain)

        dfs(1, n)
        return res


Solution().combinationSum3(3, 7)
Solution().combinationSum3(3, 9)
