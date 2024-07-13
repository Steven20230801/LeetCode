from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}
        ans = k + 1
        for i in range(len((nums))):

            if nums[i] not in h:
                h[nums[i]] = i  # 最左邊下標
            else:
                ans = min(ans, i - h[nums[i]])
                h[nums[i]] = i  # 更新下標

        if ans < k + 1:
            return True
        else:
            return False


Solution().containsNearbyDuplicate([1, 0, 1, 1], 1)
