from typing import List


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 初始化最大可達位置為0
        max_reach = 0
        # 目標位置為陣列的最後一個索引
        target = len(nums) - 1

        # 遍歷每一個位置和對應的跳躍步數
        for pos, jump in enumerate(nums):
            # 如果當前的位置大於之前能夠跳到的最遠位置，表示無法繼續前進
            if max_reach < pos:
                return False  # 矛盾：無法到達當前的位置
            else:
                # 如果當前的位置在可達範圍內，更新最大可達位置
                max_reach = max(max_reach, pos + jump)  # 更新最遠可達位置

            # 如果最遠可達位置已經達到或超過目標，返回True
            if max_reach >= target:
                return True

        # 遍歷完所有位置後，如果最遠可達位置達不到目標，返回False
        return max_reach >= target


Solution().canJump(nums=[2, 3, 1, 1, 4])
Solution().canJump(nums=[3, 2, 1, 0, 4])
