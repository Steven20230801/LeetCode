from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # 找出最小的兩個 and 最大的兩個
        min_ = [float("inf"), float("inf")]
        max_ = [0, 0]

        for x in nums:
            if x < min_[1]:  # 更新最小值
                if x < min_[0]:
                    min_[1] = min_[0]
                    min_[0] = x
                else:
                    min_[1] = x
            if x > max_[0]:
                if x > max_[1]:
                    max_[0] = max_[1]
                    max_[1] = x
                else:
                    max_[0] = x

        return max_[0] * max_[1] - min_[0] * min_[1]


test1 = [5, 6, 7, 2, 4]
test2 = [1, 2, 1, 1]

Solution().maxProductDifference(test1)
Solution().maxProductDifference(test2)
