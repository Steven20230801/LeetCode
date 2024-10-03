# 45. Jump Game II
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # 如果陣列只有一個元素，已經在起始位置，無需跳躍
        if len(nums) == 1:
            return 0

        # 初始化變數
        max_reach = 0  # 當前跳躍能達到的最遠位置
        target = len(nums) - 1  # 目標位置為陣列的最後一個索引
        res = 0  # 記錄跳躍次數
        cur = 0  # 當前跳躍範圍的起始位置

        # 當前跳躍範圍內的位置進行遍歷
        while cur <= max_reach:
            max_reach_prev = max_reach  # 記錄此次跳躍前的最遠可達位置
            res += 1  # 每進行一次跳躍，跳躍次數加一

            # 遍歷當前跳躍範圍內的所有位置
            for pos in range(cur, max_reach + 1):
                jump = nums[pos]  # 從當前位置能跳躍的步數
                max_reach = max(max_reach, pos + jump)  # 更新最遠可達位置

                # 如果最遠可達位置已經達到或超過目標，返回跳躍次數
                if max_reach >= target:
                    return res

            cur = max_reach_prev + 1  # 更新下一次跳躍的起始位置

        # 理論上不會到達這裡，因為問題保證可以到達最後一個位置
        return res


Solution().canJump(nums=[2, 3, 1, 1, 4])
Solution().canJump(nums=[2, 3, 0, 1, 4])
