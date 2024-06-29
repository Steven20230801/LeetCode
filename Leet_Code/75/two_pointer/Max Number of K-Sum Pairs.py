from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        h = {}
        l = 0
        ans = 0
        while l < len(nums):
            # 1 ->

            # 找到匹配值且還有剩餘
            if k - nums[l] in h and h[k - nums[l]] > 0:
                h[k - nums[l]] -= 1
                ans += 1
            else:
                # 如果不再同時nums[l]又出現一次的話
                if nums[l] in h:
                    h[nums[l]] += 1
                else:
                    h[nums[l]] = 1

            l += 1
        return [ans, h]
        # nums - k


Solution().maxOperations(nums=[1, 2, 4, 3], k=6)


Solution().maxOperations(nums=[3, 3, 3, 3], k=6)


Solution().maxOperations(nums=[2, 1, 1, 1, 2, 2, 2], k=3)
