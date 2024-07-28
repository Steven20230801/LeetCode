from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:

            m = (l + r) // 2
            # check m左邊與右邊
            # 1. mid = 左邊界, 只要檢查右邊
            # 2. mid = 右邊界, 只要檢查左邊
            if (m == 0 or nums[m] != nums[m - 1]) and (m == len(nums) - 1 or nums[m] != nums[m + 1]):
                return nums[m]

            # 檢查左邊長度 若整除2說明左邊沒有答案
            if nums[m] == nums[m - 1]:
                left_size = len(nums[: m - 1])
            else:
                left_size = len(nums[:m])

            if left_size % 2 == 0:
                l = m + 1
            else:
                r = m - 1


Solution().singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 5, 5])
Solution().singleNonDuplicate(nums=[1, 1, 2, 2, 4])
Solution().singleNonDuplicate(nums=[1, 2, 2, 4, 4])
