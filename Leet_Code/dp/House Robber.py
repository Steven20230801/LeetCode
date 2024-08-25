from functools import cache
from typing import List


# Back Tracking
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        @cache
        def dfs(i):
            if i < 0:
                return 0
            res = max(dfs(i - 1), dfs(i - 2) + nums[i])
            return res

        return dfs(n - 1)


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        path = [-1] * n

        def dfs(i):
            if i < 0:
                return 0
            if path[i] != -1:
                return path[i]
            res = max(dfs(i - 1), dfs(i - 2) + nums[i])
            return res

        return dfs(n - 1)


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        path = [-1] * n

        def dfs(i):
            if i < 0:
                return 0
            if path[i] != -1:
                return path[i]
            res = max(dfs(i - 1), dfs(i - 2) + nums[i])
            path[i] = res
            return res

        return dfs(n - 1)


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        path = [-1] * n

        def dfs(i):
            if i < 0:
                return 0
            if path[i] != -1:
                return path[i]
            res = max(dfs(i - 1), dfs(i - 2) + nums[i])
            path[i] = res
            return res

        return dfs(n - 1)


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        path = [nums[0], max(nums[0], nums[1])] + [-1] * n
        for i in range(2, n):
            path[i] = max(path[i - 2] + nums[i], path[i - 1])

        return path[n - 1]


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        path = [nums[0], max(nums[0], nums[1])]
        for i in range(2, n):
            temp = path[1]
            path[1] = max(path[0] + nums[i], path[1])
            path[0] = temp

        return path[1]


Solution().rob([1, 2, 3, 1])
Solution().rob([1, 1])
Solution().rob([2, 7, 9, 3, 1])
