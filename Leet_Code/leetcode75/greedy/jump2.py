from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        jumps = 0
        next_cover = 0
        cur = 0
        for i in range(len(nums)):

            next_cover = max(next_cover, i + nums[i])

            if i == cur and cur != len(nums) - 1:
                jumps += 1
                cur = next_cover

                if next_cover >= len(nums) - 1:  # 最大覆蓋範圍已經碰到了

                    return jumps


class Solution:
    def jump(self, nums: List[int]) -> int:
        # 首先從0開始, 0的Jump代表後面 0~0 + jump的下標都可以當作下次的起跳點
        # 遍歷下一次的起跳點, 計算下下次可以達到的最大下標
        if len(nums) == 1:
            return 0

        st, ed = 0, 0  # 初始的起跳點
        max_cover = 0  # 最大覆蓋範圍
        jumps = 0  # 目前跳了幾次
        while ed <= len(nums) - 1:

            for i in range(st, ed + 1):  # 針對這次的起跳範圍做測試

                max_cover = max(max_cover, i + nums[i])  # 更新最遠距離

            # 遍例完後將起跳範圍更新到下下次的範圍(不要再跳有跳過的下標)
            st = ed + 1
            ed = max_cover
            jumps += 1

            # 如果max_cover已經到了最大下標就直接返回

            if max_cover >= len(nums) - 1:
                return jumps


Solution().jump([2, 3, 1, 1, 4])


Solution().jump([2, 3])


Solution().jump([1, 2, 1, 1, 1])


Solution().jump([7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3])

Solution().jump([0])
