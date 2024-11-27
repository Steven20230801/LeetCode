from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)  # 獲取陣列長度
        max_prod = [0] * n  # 初始化最大乘積陣列
        min_prod = [0] * n  # 初始化最小乘積陣列

        max_prod[0] = nums[0]  # 初始最大乘積為第一個元素
        min_prod[0] = nums[0]  # 初始最小乘積為第一個元素
        res = nums[0]  # 初始化結果為第一個元素

        # 從第二個元素開始遍歷陣列
        for i in range(1, n):
            # 計算以當前元素結尾的最大乘積
            max_prod[i] = max(nums[i], max_prod[i - 1] * nums[i], min_prod[i - 1] * nums[i])  # 單獨當前元素  # 與前一個最大乘積相乘  # 與前一個最小乘積相乘（考慮負數情況）

            # 計算以當前元素結尾的最小乘積
            min_prod[i] = min(nums[i], max_prod[i - 1] * nums[i], min_prod[i - 1] * nums[i])  # 單獨當前元素  # 與前一個最大乘積相乘  # 與前一個最小乘積相乘

            # 更新全局最大乘積
            res = max(res, max_prod[i])

            # 以下為調試用的打印語句（已註解掉）
            # print(f"---------{i}---------")
            # print(f"res:{res}")
            # print(f"max_prod:{max_prod}")
            # print(f"min_prod:{min_prod}")
            # print(f"---------{i}---------")

        return res  # 返回全局最大乘積


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res, cur_min_prod, cur_max_prod = nums[0], nums[0], nums[0]
        for i in range(1, n):

            cur_min = min(nums[i], cur_min_prod * nums[i], cur_max_prod * nums[i])
            cur_max = max(nums[i], cur_min_prod * nums[i], cur_max_prod * nums[i])
            res = max(res, cur_max)
            cur_min_prod, cur_max_prod = cur_min, cur_max
        return res


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res, cur_min_prod, cur_max_prod = nums[0], nums[0], nums[0]
        for i in range(1, n):
            if nums[i] < 0:
                cur_min_prod, cur_max_prod = cur_max_prod, cur_min_prod
            cur_max_prod = max(nums[i], cur_max_prod * nums[i])
            cur_min_prod = min(nums[i], cur_min_prod * nums[i])
            res = max(res, cur_max_prod)
        return res


Solution().maxProduct([2, 3, -2, 4])
Solution().maxProduct([-2, -3, -4])
Solution().maxProduct([-2, 0, -1])
Solution().maxProduct([-2])
