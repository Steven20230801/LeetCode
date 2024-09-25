from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        ans = []
        path = []
        n = len(nums)

        def dfs(i):
            if i == n:
                if len(path) >= 2:
                    ans.append(path.copy())
                return

            used = set()

            for j in range(i, n):
                if nums[j] in used:
                    continue  # 如果这个元素已经被使用过，则跳过

                if not path or nums[j] >= path[-1]:
                    used.add(nums[j])
                    path.append(nums[j])
                    dfs(j + 1)
                    path.pop()

        dfs(0)

        return ans


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        ans = []
        path = []
        n = len(nums)

        def dfs(i):
            if i == n:
                if len(path) >= 2:
                    ans.append(path.copy())
                return

            used = set()  # 记录当前层已经使用过的元素

            for j in range(i, n):
                if nums[j] in used:
                    continue  # 如果这个元素已经被使用过，则跳过

                if not path or nums[j] >= path[-1]:  # 确保非严格递增
                    used.add(nums[j])  # 记录当前元素
                    path.append(nums[j])
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return ans


Solution().findSubsequences([1, 2])
Solution().findSubsequences([4, 4, 3, 2, 1])
Solution().findSubsequences([4, 6, 7, 7])
