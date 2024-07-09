from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums) - 1
        l = 0
        ans = []

        def dfs(i, l=0):  # i 代表到了第幾個下標

            if i >= n:
                ans.append(l)
                return

            if nums[i] == 0:
                return

            for x in range(1, nums[i] + 1):

                dfs(i + x, l=l + x)

        dfs(0)

        return ans, n in ans


Solution().canJump(nums=[2, 3, 1, 1, 4])

Solution().canJump(nums=[2, 3, 0, 0, 4])

Solution().canJump(nums=[2, 0, 0])
