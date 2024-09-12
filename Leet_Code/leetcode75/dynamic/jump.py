from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxn = 0  # 能跳到最遠的位子

        for i, jump in enumerate(nums):

            # 如果最大位子到的了I的話
            if maxn >= i and i + jump > maxn:
                # 更新
                maxn = i + jump
            if i > maxn:
                return False
            if maxn >= len(nums) - 1:
                return True


# dp 解法
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        jumped = [False] * n  # 紀錄是否已經跳過這個位子了

        def dfs(i):

            # base case: 若已經跳到最後一個位子了-> 回傳True
            if i >= n - 1:
                return True

            if jumped[i]:  # 若跳到已經查看過的, 就回傳
                return False

            jumped[i] = True  # 記錄此位子已經測試過
            max_jumps = min(i + nums[i], n - 1)

            for j in range(i + 1, max_jumps + 1):
                if dfs(j):
                    return True

            return False

        return dfs(0)


Solution().canJump(nums=[2, 3, 1, 1, 4])

Solution().canJump(nums=[3, 2, 0, 0, 4])

Solution().canJump(nums=[2, 0, 0])


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1  # last index

        for i in reversed(range(len(nums))):
            if i + nums[i] >= target:
                target = i
        return target == 0


Solution().canJump(nums=[2, 3, 0, 0, 4])
