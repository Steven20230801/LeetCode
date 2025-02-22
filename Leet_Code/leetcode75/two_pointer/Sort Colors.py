from collections import Counter


class Solution:
    def sortColors(self, nums):

        counter = Counter(nums)

        l = 0

        for x in [0, 1, 2]:
            while x in counter and counter[x] > 0:
                nums[l] = x
                l += 1
                counter[x] -= 1


class Solution:
    def sortColors(self, nums):

        cur, l, r = 0, 0, len(nums) - 1  # l左邊代表都是0, r右邊代表都是2

        while cur <= r:

            # 確認目前的數字跟2比較, 是否要跟r指針交換
            if nums[cur] == 2:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
                continue
            # 確認目前的數字跟0比較, 是否要跟l指針交換
            if nums[cur] == 0:
                nums[cur], nums[l] = nums[l], nums[cur]
                l += 1

            cur += 1
        return nums


Solution().sortColors(nums=[2, 0, 2, 1, 1, 0])
Solution().sortColors(nums=[2, 0, 1])
Solution().sortColors(nums=[2, 1, 2])


class Solution:
    def sortColors(self, nums):

        counter = Counter(nums)

        l = 0

        for x in [0, 1, 2]:
            while x in counter and counter[x] > 0:
                nums[l] = x
                l += 1
                counter[x] -= 1


class Solution:
    def sortColors(self, nums):
        # quick select
        cur, l, r = 0, 0, len(nums) - 1
        # <l -> 都為0
        # >r -> 都為2
        while cur <= r:

            if nums[cur] == 2:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
            elif nums[cur] == 0:
                nums[cur], nums[l] = nums[l], nums[cur]
                l += 1
                # cur += 1
            else:
                cur += 1

        return nums


Solution().sortColors(nums=[2, 0, 2, 1, 1, 0])
Solution().sortColors(nums=[2, 0, 1])
Solution().sortColors(nums=[2, 1, 2])
