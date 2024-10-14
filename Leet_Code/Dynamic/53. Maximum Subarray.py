from typing import List


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 初始化當前子陣列的和和最大子陣列和為第一個元素
        cur = nums[0]
        cur_max = nums[0]

        # 從第二個元素開始遍歷
        for x in nums[1:]:
            # 如果當前累計和為負數，則重置為當前元素
            # 否則，將當前元素加到累計和中
            cur = max(x, cur + x)

            # 更新最大子陣列和
            cur_max = max(cur_max, cur)

        return cur_max


Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
Solution().maxSubArray(nums=[1])
Solution().maxSubArray(nums=[5, 4, -1, 7, 8])
