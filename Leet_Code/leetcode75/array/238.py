from typing import List


nums = [1, 2, 3, 4]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        temp = 1
        # 先循環一次算prefix prod
        prefix = [1]  # 一開始的1 最左邊設置1
        for i in range(len(nums)):
            temp *= nums[i]
            prefix.append(temp)

        postfix = [1]  # 一開始的1 最左邊設置1
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            temp *= nums[i]
            postfix.append(temp)

        ans = []

        for i in range(len(nums)):
            ans.append(prefix[i] * postfix[len(nums) - i - 1])

        return ans


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        temp = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] *= temp
            temp *= nums[i]

        # 此時temp = list元素相乘, 每個res[i]為res[0] - res[i] 相乘

        temp = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= temp
            temp *= nums[i]  # 反向cum prod

        return res
